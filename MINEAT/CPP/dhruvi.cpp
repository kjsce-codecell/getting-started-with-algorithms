#include <bits/stdc++.h>
#include <stdio.h>
#define ll long long

using namespace std;

bool possible(ll k, ll a[], ll h, ll n) {
    ll e = 0;
    for(ll i = 0; i < n; i++) {
    	e += a[i] / k + min(a[i] % k, 1LL);
    }
    if(e <= h) 
      return true;
    else 
      return false;
}

int bsearch(ll a[], ll n, ll h) {
    ll s = 1, ed = *max_element(a, a + n), ans;
    while(s <= ed) {
        ll mid = (s + ed) / 2;
        if(possible(mid, a, h, n)) {
            ed = mid - 1;
            ans = mid;
        }
        else {
            s = mid + 1;
        }
    }
    return ans;
}
int main() {
    ll t, n, h; 
    cin >> t;
    for(ll i = 0; i<t; i++) {
        cin >> n >> h;
        ll a[n]; for(ll i = 0; i < n; i++) cin >> a[i];
        ll res = bsearch(a, n, h);
        cout << res << "\n";
    }
}
