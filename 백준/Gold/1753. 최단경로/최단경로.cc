#include <iostream>
#include <vector>
#include <climits>
#include <queue>

using namespace std;
int V, E, k;
vector<pair<int, int>>graph[20001];
vector<int>d(20001, INT_MAX);

void dijkstra() {
	priority_queue<pair<int, int>>pq;
	d[k] = 0;
	pq.push({ 0,k });

	while (!pq.empty()) {
		int current_node =  pq.top().second;
		int current_node_distance = - pq.top().first;
		pq.pop();

		if (d[current_node] < current_node_distance) continue;

		for (int i = 0; i < graph[current_node].size(); i++) {
			int next_node = graph[current_node][i].first;
			int next_node_distance = graph[current_node][i].second + current_node_distance;

			if (next_node_distance < d[next_node]) {
				d[next_node] = next_node_distance;
				pq.push({ -next_node_distance, next_node });
			}
		}
	}

	for (int i = 1; i < V + 1; i++) {
		if (d[i] == INT_MAX) cout << "INF\n";
		else cout << d[i] << "\n";
	}
}

int main() {
	cin >> V >> E;
	cin >> k;
	for (int i = 0; i < E; i++) {
		int u, v, w;
		cin >> u >> v >> w;
		graph[u].push_back({ v,w });
	}
	dijkstra();
	return 0;
}