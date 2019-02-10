N = 10005

marker = [0]*N
PRIMES = []
levy = [0]*N

# PRECAL PRIMES
marker[0] = marker[1] = 1   # marked non primes
for i in range(2, int(N**0.5)):
    for j in range(i*i,N,i):
        marker[j] = 1

for i in range(N):
    if not marker[i]:
        PRIMES.append(i)

# PRECAL LEVY
n_primes = len(PRIMES)

for i in range(n_primes):
    a = PRIMES[i]
    for j in range(n_primes):
        b = PRIMES[j]
        if a + 2*b < N:
            levy[a + 2*b] += 1

# MAIN

t = int(input())

for _ in range(t):
    n = int(input())
    print(levy[n])
