#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <map>


using namespace std;

const int N = 1000;

int main() {
    vector<int> a, b;

    for (int i = 0; i < N; i++) {
        int x, y;
        cin >> x >> y;
        a.push_back(x);
        b.push_back(y);
    }

    map<int, int> freq;
    for (auto x: b) {
        freq[x]++;
    }

    long long similarity_score = 0 ;
    for (auto x: a) {
        similarity_score += x * freq[x];
    }

    cout << similarity_score << endl;

    return 0;
}

