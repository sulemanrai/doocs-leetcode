#!/usr/bin/env python3
import re
from pathlib import Path

LANGUAGES = ["cpp", "java", "py", "ts", "rb", "js"]
SOLUTION_ROOT = Path("solution")
OUTPUT_ROOT = Path("my_solutions")


def slugify(title: str) -> str:
    match = re.match(r"(\d+)\.\s+(.+)", title)
    if not match:
        return title.lower().replace(" ", "-")
    num, name = match.groups()
    return f"{num}-{name.lower().replace(' ', '-')}"


# ---------------------------------------------------------------------------
# C++ include inference
# ---------------------------------------------------------------------------

CPP_INCLUDE_MAP = [
    (r'\bvector\b',              '#include <vector>'),
    (r'\bstring\b',              '#include <string>'),
    (r'\bunordered_map\b',       '#include <unordered_map>'),
    (r'\bunordered_set\b',       '#include <unordered_set>'),
    (r'\bmap\b',                 '#include <map>'),
    (r'\bset\b',                 '#include <set>'),
    (r'\bstack\b',               '#include <stack>'),
    (r'\bqueue\b',               '#include <queue>'),
    (r'\bdeque\b',               '#include <deque>'),
    (r'\bpriority_queue\b',      '#include <queue>'),
    (r'\bpair\b',                '#include <utility>'),
    (r'\bsort\b|\breverse\b',    '#include <algorithm>'),
    (r'\bmax\b|\bmin\b',         '#include <algorithm>'),
    (r'\babs\b',                 '#include <cmath>'),
    (r'\bINT_MAX\b|\bINT_MIN\b', '#include <climits>'),
    (r'\bstringstream\b',        '#include <sstream>'),
    (r'\barray\b',               '#include <array>'),
    (r'\bbitset\b',              '#include <bitset>'),
    (r'\baccumulate\b|\biota\b', '#include <numeric>'),
]


def _infer_cpp_includes(src: str) -> str:
    """Scan source for known types/functions and return the needed #include lines."""
    seen = set()
    includes = []
    for pattern, include in CPP_INCLUDE_MAP:
        if re.search(pattern, src, re.IGNORECASE) and include not in seen:
            seen.add(include)
            includes.append(include)
    return "\n".join(includes)


# ---------------------------------------------------------------------------
# Signature extraction — reads the reference Solution.* and strips the body
# ---------------------------------------------------------------------------

def extract_cpp(prob_dir: Path, folder_slug: str) -> str:
    ref = prob_dir / "Solution.cpp"
    if ref.exists():
        src = ref.read_text()
        return _stub_cpp(src)
    return _fallback("cpp", folder_slug)


def extract_java(prob_dir: Path, folder_slug: str) -> str:
    ref = prob_dir / "Solution.java"
    if ref.exists():
        src = ref.read_text()
        return _stub_body(src, "java")
    return _fallback("java", folder_slug)


def extract_py(prob_dir: Path, folder_slug: str) -> str:
    ref = prob_dir / "Solution.py"
    if ref.exists():
        src = ref.read_text()
        return _stub_py(src)
    return _fallback("py", folder_slug)


def extract_ts(prob_dir: Path, folder_slug: str) -> str:
    ref = prob_dir / "Solution.ts"
    if ref.exists():
        src = ref.read_text()
        return _stub_ts(src)
    return _fallback("ts", folder_slug)


def extract_js(prob_dir: Path, folder_slug: str) -> str:
    ref = prob_dir / "Solution.js"
    if ref.exists():
        src = ref.read_text()
        return _stub_js(src)
    return _fallback("js", folder_slug)


def extract_rb(prob_dir: Path, folder_slug: str) -> str:
    ref = prob_dir / "Solution.rb"
    if ref.exists():
        src = ref.read_text()
        return _stub_rb(src)
    return _fallback("rb", folder_slug)


# ---------------------------------------------------------------------------
# Language-specific body stubbers
# ---------------------------------------------------------------------------

def _stub_cpp(src: str) -> str:
    """Infer includes from reference source, keep class + method signature, stub body."""
    sig_re = re.compile(
        r"((?:[ \t]+)(?:[\w:<>*&,\s]+)\s+\w+\s*\([^)]*\)\s*\{)",
        re.MULTILINE
    )
    m = sig_re.search(src)
    if not m:
        return src

    indent = re.match(r"(\s*)", m.group(0)).group(1)
    includes = _infer_cpp_includes(src)

    class_start = re.search(r"^class\s+", src, re.MULTILINE)
    class_and_sig = src[class_start.start():m.end()] if class_start else src[:m.end()]

    return (
        includes + "\nusing namespace std;\n\n" +
        class_and_sig.rstrip() +
        "\n" + indent + "    // TODO: implement\n" +
        indent + "}\n};\n"
    )


def _stub_body(src: str, lang: str) -> str:
    """
    For Java: keep everything up to and including the opening brace of the
    public method, replace the body with a TODO comment, close braces.
    """
    sig_re = re.compile(
        r"((?:[ \t]+)public\s+[\w\[\]<>,\s]+\s+\w+\s*\([^)]*\)\s*\{)",
        re.MULTILINE
    )

    m = sig_re.search(src)
    if not m:
        return src

    before = src[:m.end()]
    indent = re.match(r"(\s*)", m.group(0)).group(1)

    stub = before.rstrip() + "\n" + indent + "    // TODO: implement\n" + indent + "}\n}\n"

    # Preserve Java imports at the top
    imports = re.findall(r'^import .+;$', src, re.MULTILINE)
    if imports and not stub.startswith("import"):
        stub = "\n".join(imports) + "\n\n" + stub.lstrip()

    return stub


def _stub_py(src: str) -> str:
    """Keep class/def signature lines, stub the body."""
    lines = src.splitlines()
    output = []
    in_body = False
    indent_level = None

    for line in lines:
        stripped = line.lstrip()

        if stripped.startswith("class Solution") or stripped.startswith("def "):
            output.append(line)
            in_body = False
            indent_level = None
            continue

        if output and not in_body:
            if stripped and indent_level is None:
                indent_level = len(line) - len(stripped)
                output.append(" " * indent_level + "# TODO: implement")
                output.append(" " * indent_level + "pass")
                in_body = True
            continue

        if in_body:
            if line.strip() == "" or (line and len(line) - len(line.lstrip()) >= indent_level):
                continue
            else:
                in_body = False
                output.append(line)

    return "\n".join(output) + "\n"


def _stub_ts(src: str) -> str:
    """Stub TypeScript function body."""
    m = re.search(r"(function\s+\w+\s*\([^)]*\)\s*(?::\s*[\w\[\]<>|,\s]+)?\s*\{)", src, re.DOTALL)
    if not m:
        return src
    return m.group(1).rstrip() + "\n    // TODO: implement\n};\n"


def _stub_js(src: str) -> str:
    """Stub JavaScript function body."""
    m = re.search(r"((?:var\s+\w+\s*=\s*function|function\s+\w+)\s*\([^)]*\)\s*\{)", src, re.DOTALL)
    if not m:
        return src
    return m.group(1).rstrip() + "\n    // TODO: implement\n};\n"


def _stub_rb(src: str) -> str:
    """Stub Ruby method body."""
    m = re.search(r"(def\s+\w+[^\n]*\n)", src)
    if not m:
        return src
    return m.group(1) + "  # TODO: implement\nend\n"


def _fallback(lang: str, folder_slug: str) -> str:
    return f"// No reference Solution found for {lang} — {folder_slug}\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

EXTRACTORS = {
    "cpp":  extract_cpp,
    "java": extract_java,
    "py":   extract_py,
    "ts":   extract_ts,
    "js":   extract_js,
    "rb":   extract_rb,
}


def main():
    if not SOLUTION_ROOT.exists():
        print(f"❌ Solution root not found: {SOLUTION_ROOT}")
        return

    range_dirs = [
        d for d in SOLUTION_ROOT.iterdir()
        if d.is_dir() and re.match(r"\d{4}-\d{4}", d.name)
    ]
    total = 0

    for range_dir in sorted(range_dirs):
        for prob_dir in sorted(range_dir.iterdir()):
            if not prob_dir.is_dir():
                continue
            folder_slug = slugify(prob_dir.name)
            target_dir = OUTPUT_ROOT / folder_slug
            target_dir.mkdir(parents=True, exist_ok=True)

            for lang in LANGUAGES:
                filepath = target_dir / f"solution.{lang}"
                if filepath.exists():
                    continue
                extractor = EXTRACTORS[lang]
                content = extractor(prob_dir, folder_slug)
                filepath.write_text(content)
                print(f"✅ Created {filepath}")
            total += 1

    print(f"\n🎉 Processed {total} problems → {OUTPUT_ROOT}/")


if __name__ == "__main__":
    main()