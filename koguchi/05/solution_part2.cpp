#include <bits/stdc++.h>

using namespace std;

void readInput(const string &filename, unordered_map<int, vector<int>> &graph,
               vector<vector<int>> &updates)
{
    ifstream file(filename);
    string line;
    bool isRules = true;

    while (getline(file, line))
    {
        if (line.empty())
        {
            isRules = false;
            continue;
        }

        if (isRules)
        {
            // Parse rules of the format "X|Y"
            istringstream ruleStream(line);
            int x, y;
            char delimiter;
            if (ruleStream >> x >> delimiter >> y && delimiter == '|')
            {
                graph[x].push_back(y);
            }
        }
        else
        {
            // Parse updates for the pages "X,Y,Z,..."
            istringstream updateStream(line);
            vector<int> update;
            int page;
            char delimiter;
            while (updateStream >> page)
            {
                update.push_back(page);
                updateStream >> delimiter;
            }
            updates.push_back(update);
        }
    }

    file.close();
}

vector<int>
sortUpdateTopologically(const vector<int> &update,
                        const unordered_map<int, vector<int>> &graph)
{
    // Build in-degree map for nodes in the update
    unordered_map<int, int> inDegree;
    for (int page : update)
    {
        inDegree[page] = 0; // Initialize in-degree to 0
    }

    // Populate in-degrees based on the rules graph
    for (const auto &[key, neighbors] : graph)
    {
        for (int neighbor : neighbors)
        {
            if (inDegree.find(key) != inDegree.end() &&
                inDegree.find(neighbor) != inDegree.end())
            {
                inDegree[neighbor]++;
            }
        }
    }

    // Perform Kahn's algorithm
    queue<int> q;
    for (const auto &[node, degree] : inDegree)
    {
        if (degree == 0)
        {
            q.push(node);
        }
    }

    vector<int> sortedOrder;
    while (!q.empty())
    {
        int node = q.front();
        q.pop();
        sortedOrder.push_back(node);

        for (int neighbor : graph.at(node))
        {
            if (inDegree.find(neighbor) != inDegree.end())
            {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0)
                {
                    q.push(neighbor);
                }
            }
        }
    }

    // If sortedOrder doesn't include all nodes, the graph is invalid (shouldn't
    // happen here)
    if (sortedOrder.size() != update.size())
    {
        cerr << "Error: Unable to sort update, possible cycle in input!"
             << endl;
    }

    return sortedOrder;
}

int main()
{
    unordered_map<int, vector<int>> graph;
    vector<vector<int>> updates;

    readInput("input.txt", graph, updates);

    int totalMiddleSum = 0;

    cout << "Sorting updates..." << endl;
    for (const auto &update : updates)
    {
        cout << "Original Update: ";
        for (int page : update)
        {
            cout << page << " ";
        }

        vector<int> sortedUpdate = sortUpdateTopologically(update, graph);

        cout << "\nSorted Update:   ";
        for (int page : sortedUpdate)
        {
            cout << page << " ";
        }

        // Add the middle term of the sorted update to the total sum
        int middleIndex = sortedUpdate.size() / 2;
        totalMiddleSum += sortedUpdate[middleIndex];

        cout << "(Middle term: " << sortedUpdate[middleIndex] << ")" << endl;
    }

    cout << "\nTotal sum of middle terms for sorted updates: " << totalMiddleSum
         << endl;

    // (All mid)8530 - (mid part 1)3608 = (mid part 2)4922

    return 0;
}
