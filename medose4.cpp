#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

// moving avg
vector<int> mkFilter(const vector<int>& data, int grp_size) {
    vector<int> smoothed;
    for (size_t i = 0; i <= data.size() - grp_size; i++) {
        int sum = 0;
        for (size_t j = i; j < i + grp_size; j++) {
            sum += data[j];
        }
        smoothed.push_back(sum / grp_size);
    }
    return smoothed;
}

// median filter
vector<int> skFilter(const vector<int>& data, int grp_size) {
    vector<int> smoothed;
    for (size_t i = 0; i <= data.size() - grp_size; i++) {
        vector<int> grp(data.begin() + i, data.begin() + i + grp_size);
        sort(grp.begin(), grp.end());
        smoothed.push_back(grp[grp_size / 2]);  // Median value
    }
    return smoothed;
}

int main() {
    ifstream file("log.txt");
    vector<int> data;
    int num;

    // get and read the data from the log.txt file
    while (file >> num) {
        data.push_back(num);
    }
    file.close();

    int grp_size = 3;  // group size

    // Apply filters
    vector<int> mkResult = mkFilter(data, grp_size);
    vector<int> skResult = skFilter(data, grp_size);

    cout << "Original Data: ";
    for (int val : data) cout << val << " ";
    cout << "\nMK Filter Output: ";
    for (int val : mkResult) cout << val << " ";
    cout << "\nSK Filter Output: ";
    for (int val : skResult) cout << val << " ";
    
    cout << endl;
    return 0;
}

