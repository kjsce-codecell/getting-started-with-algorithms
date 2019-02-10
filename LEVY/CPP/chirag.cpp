#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long ll;
ll a[10001], cnt[10001], i;
vector<ll> primes;

void seive()
{
	a[0] = 1;
	a[1] = 1;
	for (ll i = 2; i < 10001; i++)
	{
		if (a[i] == 0)
		{
			primes.push_back(i);
			for (ll j = i; (i * j) < 10001; j++)
				a[i * j] = 1;
		}
	}
}

void solve()
{
	cin >> i;
	cout << cnt[i] << "\n";
}

int main()
{
	ll t;
	cin >> t;
	seive();
	for (ll i = 0; i < primes.size(); i++)
	{
		for (ll j = i; j < primes.size(); j++)
		{
			ll k = primes[i];
			ll l = primes[j];
			if (k + (2 * l) <= 10000)
				cnt[k + (2 * l)]++;
			if (k != l)
			{
				if (l + (2 * k) <= 10000)
					cnt[l + (2 * k)]++;
			}
		}
	}
	while (t--)
		solve();
}
