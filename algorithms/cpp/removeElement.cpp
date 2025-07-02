#include <iostream>
#include <vector>
#include <unordered_map>


using namespace std;


class Solution {
public:
    /*
    Removes all instances of 'val' in-place by swapping with end elements.
    Returns the new length of the array after removal.
    Uses two pointers: left (i) and right (c), with k counting removals.
    */
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        int c = nums.size() - 1;
        int k = 0;
        while (i <= c) {
            if (nums[c] == val) {
                c--;
                k++;
                continue;
            }
            if (nums[i] == val) {
                int tmp = nums[i];
                nums[i] = nums[c];
                nums[c] = tmp;
                k++;
                c--;
            }
            i++;
        }
        return nums.size() - k;
    }
};
