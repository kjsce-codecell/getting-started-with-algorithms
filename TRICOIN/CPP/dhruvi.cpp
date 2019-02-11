#include <bits/stdc++.h>
#include <stdio.h>
#define ll long long
using namespace std;

int main() {
	int t,i;
	cin>>t;
	for(i=0;i<t;i++){
	    ll n;
	    cin>>n;
	    int r=sqrt((8*n)+1);
	    cout<<(r-1)/2;
	    cout<<endl;
	}
	return 0;
}

