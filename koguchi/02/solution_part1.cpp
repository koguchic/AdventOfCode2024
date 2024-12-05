#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <sstream>


using namespace std;

const int NUM_REPORTS = 1000;
const int UPPER_BOUND = 3;
const int LOWER_BOUND = 1;


int main() {

    vector<vector<int>> reports;

    string line;
    while (getline(cin, line)) {
        vector<int> report;
        istringstream iss(line);

        int level;
        while (iss >> level) {
            report.push_back(level);
        }
        reports.push_back(report);
    }

    int numSafe = NUM_REPORTS;
    for (auto report: reports) {
        bool isDescending = report[0] > report[1];

        for (int i=1; i<report.size(); i++) {
            cout << report[i-1] << ' ' << report[i] << " - ";

            // Changes direction
            if (isDescending) {
                if (report[i] > report[i-1]) {
                    numSafe--;
                    break;
                }
            }
            else {
                if (report[i] < report[i-1]) {
                    numSafe--;
                    break;
                }
            }

            // Safe levels
            int levelDiff = abs(report[i] - report[i-1]);
            if (levelDiff > UPPER_BOUND || levelDiff < LOWER_BOUND) {
                numSafe--;
                break;
            }
        }

        cout << "Num Safe: " << numSafe << endl;
    }

    return 0;
}

