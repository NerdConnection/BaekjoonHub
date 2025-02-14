#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector < pair<int, pair<int, int>>> graph;
vector <int> parents(10000, 0);

int find(int x) {
	if (parents[x] == x) return x;
	return parents[x] = find(parents[x]);
}

void uni(int x, int y) {
	x = find(x);
	y = find(y);
	if (x < y) parents[y] = x;
	else parents[x] = y;
}

int main() {
	int V, E;
	int parent, child, weight;
	int res = 0;
	cin >> V >> E;
	for (int i = 0; i < E; i++) {
		cin >> parent >> child >> weight;
		graph.push_back({ weight, {parent, child} });
	}
	
	for (int i = 0; i < V; i++) {
		parents[i] = i;
	}

	sort(graph.begin(), graph.end(), [](pair<int, pair<int, int>>a, pair<int, pair<int, int>>b) 
		{return a.first < b.first; });
	
	for (const auto & node : graph) {
		if (find(node.second.first) != find(node.second.second)) {
			uni(node.second.first, node.second.second);
			res += node.first;
		}
	}
	cout << res;
}