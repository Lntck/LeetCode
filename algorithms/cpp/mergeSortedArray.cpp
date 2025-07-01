#include <iostream>
#include <vector>
#include <unordered_map>


using namespace std;


class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int a = m - 1;
        int b = n - 1;
        int c = m + n - 1;

        // Since nums2 is addition to nums1 we go while b >= 0
        while (b >= 0) {
            if (a >= 0 && nums1[a] >= nums2[b]) {
                nums1[c--] = nums1[a--];
            } else {
                nums1[c--] = nums2[b--];
            }
        }
    }
};
