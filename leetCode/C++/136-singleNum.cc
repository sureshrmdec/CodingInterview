#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution1 {
public:
    int hashSingleNumber(vector<int>& nums) {
        unordered_map<int, bool> hash;
        for (int i = 0; i < nums.size(); i++){
            if (!hash.count(nums[i])){
               hash[nums[i]] = true;
            } else {
              hash.erase(nums[i]);
            };
        };
        return hash.begin()->first;
    }
};

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (const auto &num: nums)
            ans ^= num;
        return ans;
    }
};

int main(void){
    Solution s;
    int arr[] = {1,1,2,2,3,3,4};
    vector<int> int_arr(arr, arr + 7);
    for (vector<int>::iterator it = int_arr.begin(); it != int_arr.end(); it++) cout << *it << endl;
    cout << s.singleNumber(int_arr) << endl;
    return 0;
};
