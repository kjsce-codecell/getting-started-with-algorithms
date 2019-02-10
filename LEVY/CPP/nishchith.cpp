#include "bits/stdc++.h"
using namespace std;

#define pb push_back
#define sz(c) (int)c.size()
#define N 10010

typedef long long ll ;
typedef unsigned long long ull ;
typedef long double ld ;

vector <ll> prs, levy(N,0);
static ll arr[10010];

// PRECAL PRIMES
void primes(){
        ll i , j ;
        arr[0]=arr[1]=1;
        for(i=2;i*i<=N;i++){
        	for(j=i*i;j<=N;j+=i){
        		arr[j]=1;
        	}
        }
        for(i=0;i<N;i++)
        	if(!arr[i]){
        		prs.pb(i);
        	}
}

// PRECAL LEVY
void pre(){
        ll i , j , a, b ;
        for(i=0;i<(ll)sz(prs);++i){
                a= prs[i];
                for(j=0;j<(ll)sz(prs);++j){
                        b = prs[j];
                        if(a+2*b <N){
                        	levy[a+2*b]++;
                        }
                }
        }
}

int main(){
        ll t , n ;
        primes();
        pre();
        scanf(" %lli",&t);
        while(t--){
                scanf(" %lli", &n);
                if(n==1) 
                	printf("0\n");
                else 
                	printf("%lli\n",levy[n]);
		}
        return 0;
}
