def Prob1(n) :
    pr=[True for i in range(n+1)]
    p=2
    while(p*p <n) :
        if (pr[p] == True): 
            for i in range(p * 2, n+1, p): 
                pr[i] = False
        p += 1
    prime=[]
    for i in range(2,n) :
        if pr[i] :
            prime.append(i)
    return prime
prr=Prob1(10001)
pair=[0]*(10001)
for i in prr :
    for j in prr :
        if(i+(2*j))<=10000 :
            pair[i+(2*j)]+=1
T=int(input())
for _ in range (T) :
    N=int(input())
    print(pair[N])
