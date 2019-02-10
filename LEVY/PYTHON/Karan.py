def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    pr = []
    for i in range(2,10**4 + 1):
        if prime[i]:
            pr.append(i)
        pcount[i] = 0
    #pr contains all primes till 10**4
    #pcount is pair count for precalculating all the pairs 

    for i in pr:
        for j in pr: # counting all prime pair 
            try:
                pcount[i + 2 * j] += 1 #can also be done using if else
            except:
                continue

pcount = [0] * 10001  #init pair count to 0
SieveOfEratosthenes(10 ** 4 + 1)

#Main 
for _ in range(int(input())):
    print(pcount[int(input())])