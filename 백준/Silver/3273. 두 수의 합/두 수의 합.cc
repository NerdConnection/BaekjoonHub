#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(0), cin.tie(0);
	int n, k, x, res = 0;
	vector <pair<int,bool>> vec(1000001, pair <int, bool>(0, false));
	
	cin >> n;
	for (int idx = 0; idx < n; idx++) {
		cin >> k;
		vec[k] = pair<int,bool>(idx, true);
	}
	cin >> x;
	if (x > 1000000) {
		for (int i = x - 1000000; i < 1000001; i++) {
			if (vec[i].second == true && vec[x - i].second == true) {
				if (vec[i].first < vec[x - i].first) res++;
			}
		}
	}
	else {
		for (int i = 1; i < x; i++) {
			if (vec[i].second == true && vec[x - i].second == true) {
				if (vec[i].first < vec[x - i].first) res++;
			}
		}
	}
	cout << res;
	return 0;
}