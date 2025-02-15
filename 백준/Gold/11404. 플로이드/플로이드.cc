#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main() {
	int n, m;
	cin >> n;
	cin >> m;
	vector<vector<int>>graph(n + 1, vector<int>(n + 1, INT_MAX));
	for (int i = 1; i < n+1; i++) {
		graph[i][i] = 0;
	}

	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		graph[a][b] = min(graph[a][b], c);
	}

	for (int k = 1; k < n + 1; k++) {
		for (int i = 1; i < n + 1; i++) {
			for (int j = 1; j < n + 1; j++) {
				if (graph[i][k] != INT_MAX && graph[k][j] != INT_MAX) {
					graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
				}
			}
		}
	}

	for (int k = 1; k < n + 1; k++) {
		for (int i = 1; i < n + 1; i++) {
			if (graph[k][i] == INT_MAX) cout << "0 ";
			else cout << graph[k][i] << " ";
		}
		cout << "\n";
	}
}