#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;


class Solution {
public:
    int hIndex(vector<int>& citations) {
        // n log n
        sort(citations.begin(), citations.end(), [](int a, int b) { return a > b; });
        int hMax = 0;
        for (int i = 0; i<citations.size(); i++) {
            hMax = max(hMax, min(citations[i], i+1));
        }
        return hMax;
    }
};
