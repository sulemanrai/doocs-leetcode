#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // TODO: implement
        unordered_map<int, int> freq;
        bool ans = false;

        for(int i = 0; i < nums.size(); i++) {
            freq[nums[i]]++;
        }

        for (const auto& [_, count] : freq) {
            if(count >= 2) {
                ans = true;
                break;
            } else {
                ans = false;
            }
        }        

        return ans;
    }
};
