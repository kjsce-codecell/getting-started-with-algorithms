#include <bits/stdc++.h>
// #include <cmath>
#include <stdio.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int i,j;
	int is_prime[10001];
	int res[10001]={0};
	for(i=0;i<10001;i++)
		{
			is_prime[i]=1;
		}
		is_prime[0]=0;
		is_prime[1]=0;
		i=2;
		for(i=2;i<=100;i++)
		{
			if(is_prime[i]==1)
			{
				for(j=i*2;j<=10000;j+=i)
				{
					is_prime[j]=0;
				}
			}
		}
		for(i=2;i<=10000;i++)
		{
			if(is_prime[i]==1)
			{
				for(j=1;i+2*j<=10000;j++) 
        {
          if(is_prime[j]) 
            res[i+2*j]++;
			  }
		  }
    }
	for(i=0;i<t;i++)
	{
		int n;
		cin>>n;
		cout<<res[n]<<endl;

	}
}
