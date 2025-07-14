#include <iostream>
#include <vector>
#include <unordered_map>
#include <random>


using namespace std;


class RandomizedSet {
private:
    unordered_map<int, int> valToIndex;
    vector<int> values;
    mt19937 gen;
public:
    RandomizedSet() : gen(random_device{}()) {}
    
    bool insert(int val) {
        if (valToIndex.count(val)) { return false;}
        values.push_back(val);
        valToIndex[val] = values.size() - 1;
        return true;
    }
    
    bool remove(int val) {
        if (!valToIndex.count(val)) { return false;}
        int index = valToIndex.at(val);
        // Move the last element to the position of the element to remove
        values[index] = values[values.size() - 1];
        // Update the index of the element that was moved
        valToIndex[values[index]] = index;
        // Remove the last element from the vector
        values.pop_back();
        // Remove the element from the map
        valToIndex.erase(val);
        return true;
    }
    
    int getRandom() {
        uniform_int_distribution<int> dist(0, values.size() - 1);
        return values[dist(gen)];
    }
};
