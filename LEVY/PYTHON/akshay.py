def sieve(n):
    '''
    Sieve of eratosthenes
    Returns primesd: dictionary of primes upto n
            primesl: list of primes upto n
    '''
    l = [True]*(n+1)
    l[0] = False
    l[1] = False
    for i in range(2, n+1):
        j = i*i
        while j < n+1:
            l[j]=False
            j+=i
    primesd={}
    primesl = []
    for i in range(2, n+1):
        if l[i]:
            primesd[i]=True
            primesl.append(i)
    return primesd, primesl

primesd, primesl = sieve(10000)
pc = [0]*10001  # pc:- pair count

# pre-computing the counts for fast retreival
for e in primesl:
    for f in primesl:
        temp = e+2*f
        if temp > 10000:
            break
        pc[temp]+=1

t =int(input())

for __ in range(t):
    n = int(input())
    print(pc[n])
    