#include <iostream>
#include <vector>


using namespace std;


class Solution {
public:
    // This implementation takes the first string as the initial prefix,
    // then compares it character by character with each subsequent string.
    // If a mismatch is found, it shortens the prefix accordingly.
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = strs[0];
        for (int i=1; i<strs.size(); i++) {
            string prefixNew = "";
            for (int j=0; j<strs[i].size() && j<prefix.size(); j++) {
                if (prefix[j] == strs[i][j]) {
                    prefixNew += prefix[j];
                } else {
                    break;
                }
            }
            if (prefixNew.empty()) {
                return "";
            }
            prefix = prefixNew;
        }
        return prefix;
    }
};
