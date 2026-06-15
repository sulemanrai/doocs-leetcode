#include <vector>
using namespace std;

class TicTacToe {
private:
    int n;
    vector<vector<int>> cnt;

public:
    TicTacToe(int n)
        : n(n)
        , cnt(2, vector<int>((n << 1) + 2, 0)) {
    }

    int move(int row, int col, int player) {
        // TODO: implement
    }
};
