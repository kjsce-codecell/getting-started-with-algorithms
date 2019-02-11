#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

#define mp make_pair
#define pb push_back
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define inf LONG_LONG_MAX
#define getchar_unlocked getchar
#define F first
#define S second
#define MOD 1000000007
#define all(c) c.begin(),c.end()

ll gcd(ll x,ll y)
{
  if(y==0)
    return x;
  else
    return gcd(y,x%y);
}

void swap(ll *x,ll *y)
{
  ll temp = *x;
  *x = *y;
  *y = temp;
}

int main()
{
    vector<ll> primes;   //only prime numbers 
    ll sieve[10002] = {0};  // sieve prime numbers till 10^4
    for(int i=2;i*i<=10001;i++)
    {
        if(sieve[i] == 0)   // unmarked yet
        {
            for(int j=i*i;j<=10001;j+=i)
            {
                sieve[j] = 1;
            }
        }
    }
    for(int i=2;i<=10001;i++)
    {
        if(sieve[i] == 0)
            primes.push_back(i);
    }
    ll len = primes.size();
    //cout<<len;
    ll ans[10002] = {0};
    for(int i=0;i<len;i++)
    {
        for(int j=0;j<len;j++)
        {
            if(2*primes[i]+primes[j] <=10001)
                ans[2*primes[i]+primes[j]]++;
            else
                break;
        }
    }
    // for(int i=0;i<100;i++)
    // {
    //     cout<<ans[i]<<" ";
    // }
    int t;
    cin>>t;
    while(t--)
    {
        ll n,i,j,x,y,count=0,sum=0,max=-1;
        cin>>n;
        cout<<ans[n]<<endl;
    }    
    return 0;
}