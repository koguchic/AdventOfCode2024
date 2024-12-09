#include <bits/stdc++.h>

// #include <fstream>
// #include <iostream>
// #include <sstream>
// #include <stack>
// #include <string>
// #include <unordered_map>
// #include <unordered_set>
// #include <vector>

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

bool dfs(int node, const unordered_map<int, vector<int>> &graph,
         unordered_set<int> &visited, unordered_set<int> &recStack,
         stack<int> &topoStack)
{
    visited.insert(node);
    recStack.insert(node); // Mark node as being in the current recursion stack

    // Explore neighbors
    for (int neighbor : graph.at(node))
    {
        if (recStack.find(neighbor) != recStack.end())
        {
            // Cycle detected (not expected in this problem)
            return false;
        }
        if (visited.find(neighbor) == visited.end())
        {
            if (!dfs(neighbor, graph, visited, recStack, topoStack))
            {
                return false; // Cycle detected in a deeper level
            }
        }
    }

    recStack.erase(
        node); // Remove from recursion stack after visiting neighbors
    topoStack.push(node); // Add node to topological order stack
    return true;
}

// Perform topological sort on the graph
vector<int> topologicalSort(const unordered_map<int, vector<int>> &graph)
{
    unordered_set<int> visited;
    unordered_set<int> recStack;
    stack<int> topoStack;

    for (const auto &[node, _] : graph)
    {
        if (visited.find(node) == visited.end())
        {
            if (!dfs(node, graph, visited, recStack, topoStack))
            {
                // If a cycle is detected, return an empty result
                return {};
            }
        }
    }

    // Extract nodes from the stack to form the topological order
    vector<int> topoOrder;
    while (!topoStack.empty())
    {
        topoOrder.push_back(topoStack.top());
        topoStack.pop();
    }

    return topoOrder;
}

// Function to check if an update is already in topological order
bool isUpdateValid(const vector<int> &update,
                   const unordered_map<int, vector<int>> &graph)
{
    unordered_map<int, int> position;

    // Map each page number to its position in the update
    for (int i = 0; i < update.size(); ++i)
    {
        position[update[i]] = i;
    }

    // Check if each rule is respected within the update
    for (const auto &[key, neighbors] : graph)
    {
        for (int neighbor : neighbors)
        {
            if (position.find(key) != position.end() &&
                position.find(neighbor) != position.end())
            {
                if (position[key] >= position[neighbor])
                {
                    // Rule is violated
                    return false;
                }
            }
        }
    }

    return true;
}

int main()
{
    unordered_map<int, vector<int>> graph;
    vector<vector<int>> updates;

    readInput("input.txt", graph, updates);
    int totalMiddleSum = 0;

    cout << "Checking updates for validity..." << endl;
    for (const auto &update : updates)
    {
        bool valid = isUpdateValid(update, graph);
        cout << "Update: ";
        for (int page : update)
        {
            cout << page << " ";
        }

        if (valid)
        {
            cout << "is valid";
            // Add the middle term of the valid update to the total sum
            int middleIndex = update.size() / 2;
            totalMiddleSum += update[middleIndex];
            cout << " (Middle term: " << update[middleIndex] << ")";
        }
        else
        {
            cout << "is not valid";
        }

        cout << endl;
        cout << "\nTotal sum of middle terms for valid updates: "
             << totalMiddleSum << endl;
    }
    return 0;
}
