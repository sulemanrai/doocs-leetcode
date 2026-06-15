#!/usr/bin/env python3
import json
import subprocess
import sys
import tempfile
import argparse
import re
import shutil
from pathlib import Path

SOLUTIONS_ROOT = Path("my_solutions")
ORIGINAL_SOLUTIONS_ROOT = Path("solution")
TEST_CASES_FILE = Path("test_cases.json")
SUPPORTED_LANGUAGES = ["py", "js", "ts", "rb", "cpp", "java"]
TIMEOUT_SEC = 5
VERBOSE = True

def load_test_cases():
    if not TEST_CASES_FILE.exists():
        print(f"❌ Test cases file not found: {TEST_CASES_FILE}")
        sys.exit(1)
    with open(TEST_CASES_FILE) as f:
        return json.load(f)

def get_problem_id_from_folder(folder_name: str) -> str:
    match = re.match(r"^(\d{4})[.-]", folder_name)
    if match:
        return match.group(1)
    match = re.match(r"^(\d+)", folder_name)
    return match.group(1) if match else folder_name

def get_function_name_from_solution_code(code: str, lang: str) -> str:
    """Extract function name from original solution code."""
    if lang == "cpp":
        match = re.search(r'(?:vector<int>|bool|int|void)\s+(\w+)\s*\(', code)
    elif lang == "java":
        match = re.search(r'(?:public\s+)?(?:int\[\]|boolean|int|void)\s+(\w+)\s*\(', code)
    elif lang == "py":
        match = re.search(r'def\s+(\w+)\s*\(', code)
    elif lang == "js":
        match = re.search(r'(?:function\s+(\w+)|var\s+\w+\s*=\s*function\s*(\w+)?|const\s+\w+\s*=\s*\(.*?\)\s*=>)', code)
        if match:
            return match.group(1) or match.group(2) or "solve"
    else:
        return "solve"
    return match.group(1) if match else "solve"

def get_parameter_count(code: str, lang: str) -> int:
    """Count number of parameters in the original function signature."""
    if lang == "cpp":
        match = re.search(r'\(([^)]*)\)', code)
    elif lang == "java":
        match = re.search(r'\(([^)]*)\)', code)
    else:
        return 1  # fallback
    if not match:
        return 1
    params = match.group(1).strip()
    if not params:
        return 0
    depth = 0
    count = 1
    for ch in params:
        if ch == '<':
            depth += 1
        elif ch == '>':
            depth -= 1
        elif ch == ',' and depth == 0:
            count += 1
    return count

def get_original_solution_path(problem_id: str, lang: str) -> Path:
    """Find the original solution file for a given problem and language."""
    range_num = int(problem_id)
    lower = (range_num // 100) * 100
    upper = lower + 99
    range_folder = f"{lower:04d}-{upper:04d}"
    range_path = ORIGINAL_SOLUTIONS_ROOT / range_folder
    if not range_path.exists():
        return None
    for folder in range_path.iterdir():
        if folder.is_dir() and folder.name.startswith(problem_id):
            ext_map = {"cpp": "Solution.cpp", "java": "Solution.java", "py": "Solution.py",
                       "js": "Solution.js", "ts": "Solution.ts", "rb": "Solution.rb"}
            sol_file = folder / ext_map.get(lang, f"Solution.{lang}")
            if sol_file.exists():
                return sol_file
    return None

def generate_wrapper(lang: str, func_name: str, param_count: int, return_type: str, problem_id: str) -> str:
    """Generate a generic wrapper code snippet."""
    if lang == "py":
        return f'''
import json, sys
from solution import {func_name}

def main():
    data = json.loads(sys.stdin.read())
    result = {func_name}(*data)
    print(json.dumps(result))

if __name__ == "__main__":
    main()
'''
    elif lang == "js":
        return f'''
const {func_name} = require('./solution.js');

let data = '';
process.stdin.on('data', chunk => data += chunk);
process.stdin.on('end', () => {{
    const input = JSON.parse(data);
    const result = {func_name}(...input);
    console.log(JSON.stringify(result));
}});
'''
    elif lang == "rb":
        return f'''
require 'json'
require_relative 'solution'

data = JSON.parse(STDIN.read)
result = {func_name}(*data)
puts JSON.generate(result)
'''
    elif lang == "cpp":
        wrapper = f'''#include <iostream>
#include <string>
#include <vector>
#include <cctype>
#include <sstream>

// Helper to_json functions declared BEFORE solution.cpp and main()
std::string to_json(bool val) {{ return val ? "true" : "false"; }}
std::string to_json(int val) {{ return std::to_string(val); }}
std::string to_json(const std::vector<int>& vec) {{
    std::string out = "[";
    for (size_t i = 0; i < vec.size(); ++i) {{
        if (i > 0) out += ",";
        out += std::to_string(vec[i]);
    }}
    out += "]";
    return out;
}}

std::vector<int> parse_all_ints(const std::string& line) {{
    std::vector<int> nums;
    std::stringstream ss(line);
    char ch;
    int num;
    while (ss >> ch) {{
        if (ch == '-' || std::isdigit(ch)) {{
            ss.putback(ch);
            ss >> num;
            nums.push_back(num);
        }}
    }}
    return nums;
}}

#include "solution.cpp"

int main() {{
    std::string line;
    std::getline(std::cin, line);
    std::vector<int> all_ints = parse_all_ints(line);
    Solution sol;
    {return_type} result;
'''
        if param_count == 2:
            wrapper += f'''
    if (all_ints.size() < 2) return 1;
    int target = all_ints.back();
    std::vector<int> nums(all_ints.begin(), all_ints.end() - 1);
    result = sol.{func_name}(nums, target);
'''
        else:
            wrapper += f'''
    std::vector<int> nums = all_ints;
    result = sol.{func_name}(nums);
'''
        wrapper += f'''
    std::cout << to_json(result) << std::endl;
    return 0;
}}
'''
        return wrapper

    elif lang == "java":
        wrapper = f'''
import java.util.*;
import java.io.*;

public class Wrapper {{
    public static void main(String[] args) throws Exception {{
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String line = reader.readLine();
        List<Integer> numbers = new ArrayList<>();
        StringBuilder numBuilder = new StringBuilder();
        for (int i = 0; i < line.length(); i++) {{
            char c = line.charAt(i);
            if (c == '-' || Character.isDigit(c)) {{
                numBuilder.append(c);
            }} else if (numBuilder.length() > 0) {{
                numbers.add(Integer.parseInt(numBuilder.toString()));
                numBuilder.setLength(0);
            }}
        }}
        if (numBuilder.length() > 0) {{
            numbers.add(Integer.parseInt(numBuilder.toString()));
        }}
        Solution sol = new Solution();
        {return_type} result;
'''
        if param_count == 2:
            wrapper += f'''
        int target = numbers.get(numbers.size() - 1);
        int[] nums = new int[numbers.size() - 1];
        for (int i = 0; i < nums.length; i++) nums[i] = numbers.get(i);
        result = sol.{func_name}(nums, target);
'''
        else:
            wrapper += f'''
        int[] nums = new int[numbers.size()];
        for (int i = 0; i < nums.length; i++) nums[i] = numbers.get(i);
        result = sol.{func_name}(nums);
'''
        wrapper += f'''
        System.out.println(resultToJson(result));
    }}
    private static String resultToJson(int[] arr) {{
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < arr.length; i++) {{
            if (i > 0) sb.append(",");
            sb.append(arr[i]);
        }}
        sb.append("]");
        return sb.toString();
    }}
    private static String resultToJson(boolean b) {{
        return b ? "true" : "false";
    }}
}}
'''
        return wrapper
    else:
        return ""

def run_test(problem_id, language, solution_path, test_input, expected_output):
    input_json = json.dumps(test_input)

    original_sol_path = get_original_solution_path(problem_id, language)
    if not original_sol_path:
        func_name = get_function_name_from_solution_code("", language) or "solve"
        param_count = 1
        return_type = "auto"
    else:
        code = original_sol_path.read_text()
        func_name = get_function_name_from_solution_code(code, language)
        param_count = get_parameter_count(code, language)
        if language == "cpp":
            match = re.search(r'(vector<int>|bool|int|void)\s+' + func_name + r'\s*\(', code)
            return_type = match.group(1) if match else "auto"
        elif language == "java":
            match = re.search(r'(?:public\s+)?(int\[\]|boolean|int|void)\s+' + func_name + r'\s*\(', code)
            return_type = match.group(1) if match else "auto"
        else:
            return_type = "auto"

    if language == "py":
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            shutil.copy(solution_path, tmp_path / "solution.py")
            wrapper = generate_wrapper("py", func_name, param_count, return_type, problem_id)
            wrapper_path = tmp_path / "wrapper.py"
            wrapper_path.write_text(wrapper)
            cmd = ["python", str(wrapper_path)]
            proc = subprocess.run(cmd, input=input_json, capture_output=True, text=True, timeout=TIMEOUT_SEC)
            if proc.returncode != 0:
                return False, None, proc.stderr
            try:
                actual = json.loads(proc.stdout.strip())
                return (actual == expected_output), actual, None
            except Exception as e:
                return False, None, f"Output not valid JSON: {proc.stdout.strip()} - {e}"

    elif language == "js":
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            sol_content = solution_path.read_text()
            if f"module.exports = {func_name}" not in sol_content:
                sol_content += f"\nmodule.exports = {func_name};\n"
            sol_dest = tmp_path / "solution.js"
            sol_dest.write_text(sol_content)
            wrapper = generate_wrapper("js", func_name, param_count, return_type, problem_id)
            wrapper_path = tmp_path / "wrapper.js"
            wrapper_path.write_text(wrapper)
            cmd = ["node", str(wrapper_path)]
            proc = subprocess.run(cmd, input=input_json, capture_output=True, text=True, timeout=TIMEOUT_SEC)
            if proc.returncode != 0:
                return False, None, proc.stderr
            try:
                actual = json.loads(proc.stdout.strip())
                return (actual == expected_output), actual, None
            except Exception as e:
                return False, None, f"Output not valid JSON: {proc.stdout.strip()} - {e}"

    elif language == "ts":
        if not shutil.which("tsc"):
            return False, None, "TypeScript compiler (tsc) not found. Install with: npm install -g typescript"
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            sol_dest = tmp_path / "solution.ts"
            shutil.copy(solution_path, sol_dest)
            compile_cmd = ["tsc", "--target", "ES2020", "--module", "commonjs", str(sol_dest)]
            try:
                comp = subprocess.run(compile_cmd, capture_output=True, text=True, timeout=10)
                if comp.returncode != 0:
                    return False, None, f"TypeScript compilation failed: {comp.stderr.strip() or comp.stdout.strip()}"
                js_file = tmp_path / "solution.js"
                if not js_file.exists():
                    return False, None, "Compilation succeeded but solution.js not found"
                js_content = js_file.read_text()
                if f"module.exports = {func_name}" not in js_content:
                    js_content += f"\nmodule.exports = {func_name};\n"
                    js_file.write_text(js_content)
                wrapper = generate_wrapper("js", func_name, param_count, return_type, problem_id)
                wrapper_path = tmp_path / "wrapper.js"
                wrapper_path.write_text(wrapper)
                cmd = ["node", str(wrapper_path)]
                proc = subprocess.run(cmd, input=input_json, capture_output=True, text=True, timeout=TIMEOUT_SEC)
                if proc.returncode != 0:
                    return False, None, proc.stderr
                actual = json.loads(proc.stdout.strip())
                return (actual == expected_output), actual, None
            except subprocess.CalledProcessError as e:
                return False, None, f"TypeScript compilation failed: {e.stderr}"
            except Exception as e:
                return False, None, str(e)

    elif language == "rb":
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            shutil.copy(solution_path, tmp_path / "solution.rb")
            wrapper = generate_wrapper("rb", func_name, param_count, return_type, problem_id)
            wrapper_path = tmp_path / "wrapper.rb"
            wrapper_path.write_text(wrapper)
            cmd = ["ruby", str(wrapper_path)]
            proc = subprocess.run(cmd, input=input_json, capture_output=True, text=True, timeout=TIMEOUT_SEC)
            if proc.returncode != 0:
                return False, None, proc.stderr
            try:
                actual = json.loads(proc.stdout.strip())
                return (actual == expected_output), actual, None
            except Exception as e:
                return False, None, f"Output not valid JSON: {proc.stdout.strip()} - {e}"

    elif language == "cpp":
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            shutil.copy(solution_path, tmp_path / "solution.cpp")
            wrapper_code = generate_wrapper("cpp", func_name, param_count, return_type, problem_id)
            wrapper_file = tmp_path / "wrapper.cpp"
            wrapper_file.write_text(wrapper_code)
            exe_path = tmp_path / "wrapper.out"
            compile_cmd = ["g++", "-std=c++17", str(wrapper_file), "-o", str(exe_path)]
            try:
                subprocess.run(compile_cmd, check=True, capture_output=True, timeout=10)
                cmd = [str(exe_path)]
                proc = subprocess.run(cmd, input=input_json, capture_output=True, text=True, timeout=TIMEOUT_SEC)
                if proc.returncode != 0:
                    return False, None, proc.stderr
                actual = json.loads(proc.stdout.strip())
                return (actual == expected_output), actual, None
            except subprocess.CalledProcessError as e:
                return False, None, f"C++ compilation failed: {e.stderr.decode() if isinstance(e.stderr, bytes) else e.stderr}"
            except Exception as e:
                return False, None, str(e)

    elif language == "java":
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            shutil.copy(solution_path, tmp_path / "Solution.java")
            wrapper_code = generate_wrapper("java", func_name, param_count, return_type, problem_id)
            wrapper_file = tmp_path / "Wrapper.java"
            wrapper_file.write_text(wrapper_code)
            compile_cmd = ["javac", str(tmp_path / "Solution.java"), str(wrapper_file)]
            try:
                subprocess.run(compile_cmd, check=True, capture_output=True, timeout=10)
                cmd = ["java", "-cp", str(tmp_path), "Wrapper"]
                proc = subprocess.run(cmd, input=input_json, capture_output=True, text=True, timeout=TIMEOUT_SEC)
                if proc.returncode != 0:
                    return False, None, proc.stderr
                actual = json.loads(proc.stdout.strip())
                return (actual == expected_output), actual, None
            except subprocess.CalledProcessError as e:
                return False, None, f"Java compilation failed: {e.stderr.decode() if isinstance(e.stderr, bytes) else e.stderr}"
            except Exception as e:
                return False, None, str(e)

    else:
        return False, None, f"Unsupported language: {language}"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--problem")
    parser.add_argument("-l", "--lang")
    args = parser.parse_args()

    test_cases = load_test_cases()
    problem_folders = sorted([d for d in SOLUTIONS_ROOT.iterdir() if d.is_dir()])

    if args.problem:
        target_id = args.problem.zfill(4)
        problem_folders = [d for d in problem_folders if get_problem_id_from_folder(d.name) == target_id]
        if not problem_folders:
            print(f"❌ No folder for ID {target_id}")
            sys.exit(1)

    languages_to_test = SUPPORTED_LANGUAGES if not args.lang else [args.lang]

    total_passed = 0
    total_tests = 0

    for folder in problem_folders:
        prob_id = get_problem_id_from_folder(folder.name)
        if prob_id not in test_cases:
            if VERBOSE:
                print(f"⚠️  No test cases for {prob_id}")
            continue

        cases = test_cases[prob_id]
        inputs = cases["inputs"]
        expected = cases["outputs"]

        for lang in languages_to_test:
            sol_file = folder / f"solution.{lang}"
            if not sol_file.exists():
                if VERBOSE:
                    print(f"⚠️  No solution file for {folder.name} ({lang})")
                continue

            print(f"\n🔍 Testing {folder.name} ({lang})")
            passed_any = False
            for idx, (inp, exp) in enumerate(zip(inputs, expected)):
                passed, actual, err = run_test(prob_id, lang, sol_file, inp, exp)
                total_tests += 1
                if passed:
                    total_passed += 1
                    passed_any = True
                    print(f"  ✅ Test {idx+1} passed")
                else:
                    print(f"  ❌ Test {idx+1} failed")
                    print(f"     Input:    {inp}")
                    print(f"     Expected: {exp}")
                    print(f"     Got:      {actual}")
                    if err:
                        print(f"     Error:    {err}")
            if not passed_any:
                print(f"  💡 Hint: Ensure your solution has the same signature as the original problem.")
            print("-" * 50)

    print(f"\n📊 Summary: {total_passed}/{total_tests} tests passed")

if __name__ == "__main__":
    main()