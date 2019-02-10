def Prob(n) :
    c=0
    i=0
    while(i<=n) :
        if(n>=i+1):
            c+=1
            n-=(i+1)
        i+=1
    print(c)

T=int(input())
for _ in range(T) :
    n=int(input())
    Prob(n)