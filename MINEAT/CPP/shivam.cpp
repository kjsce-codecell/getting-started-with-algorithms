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
    int t;
    cin>>t;
    while(t--)
    {
        ll mid,l,r,n,h,i,j,x,y,count=0,sum=0,max=-1,ans=100000000000;
        cin>>n>>h;
        ll a[n];
        for(i=0;i<n;i++)
        {
            cin>>a[i];
            if(a[i]>max)
            {
                max = a[i];
            }
        }
        l = 1;
        r = max;
        while(l<=r)
        {
            mid = (l+r)/2;
            count = 0;
            for(i=0;i<n;i++)
            {
                if(a[i]<mid)
                    count+=1;
                else    
                    count+= (a[i]%mid==0)?(a[i]/mid):(a[i]/mid+1);
            }
            //cout<<count<<endl;
            if(count>h)
                l = mid+1;
            else
            {
                //cout<<ans<<" "<<mid<<endl;
                if(ans>mid)
                    ans = mid;
                r = mid-1;
            }
        }
        cout<<ans<<endl;
    }    
    return 0;
}