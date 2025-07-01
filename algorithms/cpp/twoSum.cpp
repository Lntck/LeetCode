#include <iostream>
#include <vector>
#include <unordered_map>


using namespace std;


class Solution {
public:
    /*
    * Easy simple solution is n^2 time complexity
    * ```
    * for (i in range(len(nums)))
    *   for (j in range(i+1, len(nums)))
    *       if nums[i] + nums[j] == target:
    *           return result
    * ```
    * 
    * But we can improve time complexity by using hashmap that gives o(1) for searching
    */

    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        vector<int> result;
        for (int i=0; i<nums.size(); i++) {
            if (map.find(nums[i]) == map.end()) {
                map[target - nums[i]] = i;
            } else {
                result.push_back(map.at(nums[i]));
                result.push_back(i);
                break;
            }
        }
        return result;
    }
};