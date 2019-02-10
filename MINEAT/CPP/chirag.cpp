#include <iostream>
#include <algorithm>
using namespace std;

typedef long long ll;

ll binary_search(ll a[], ll n, ll h)
{
	ll start = 1, end = a[n - 1], mid, hour, k;
	k = a[n - 1];
	while (start <= end)
	{
		mid = (start + end) / 2;
		hour = 0;
		for (ll i = 0; i < n; i++)
		{
			hour += a[i] / mid;
			if (a[i] % mid)
				hour++;
		}
		if (hour <= h)
		{
			if (k > mid)
				k = mid;
			end = mid - 1;
		}
		else
			start = mid + 1;
	}
	return k;
}

void solve()
{
	ll n, h, ans;
	cin >> n >> h;
	ll a[n];
	for (ll i = 0; i < n; i++)
		cin >> a[i];
	sort(a, a + n);
	ans = binary_search(a, n, h);
	cout << ans << "\n";
}

int main()
{
	ll t;
	cin >> t;
	while (t--)
		solve();
}
