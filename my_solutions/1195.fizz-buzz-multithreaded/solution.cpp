
using namespace std;

class FizzBuzz {
private:
    std::mutex mtx;
    atomic<int> index;
    int n;

    // 这里主要运用到了C++11中的RAII锁(lock_guard)的知识。
    // 需要强调的一点是，在进入循环后，要时刻不忘加入index <= n的逻辑
public:
    FizzBuzz(int n) {
     // TODO: implement
 }
};
