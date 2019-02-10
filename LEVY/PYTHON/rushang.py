import math
MAX = 10**4
#sieve of eratosthenes
#for finding all primes till 10000
primes = [1 for i in range(MAX)]
for i in range(2,int(math.sqrt(MAX))+1):
    if primes[i]==1:
        for j in range(i*i,MAX,i):
            primes[j] = 0

#calculating number of pairs for all possible inputs
n_pairs = [0 for i in range(MAX + 1)]
PRIMES = [x for x in range(2,len(primes)) if primes[x]==1]
for i in PRIMES:
    for j in PRIMES:
        if i + 2*j <= MAX:
            n_pairs[i + 2*j] += 1
        
for _ in range(int(input())):
    print(n_pairs[int(input())])
