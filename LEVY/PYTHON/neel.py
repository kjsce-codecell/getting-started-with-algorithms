# calculate primes
def calcPrimes(tot):
	fin = []
	primes = [1]*(tot+1)
	start = 2

	while start < tot+1:
		fin.append(start)
		
		# mark all factors of the given number		
		for i in range(2*start,tot+1,start):
			primes[i] = 0

		start +=1
		# check next unmarked number
		while start < len(primes) and primes[start] == 0:
			start += 1
	return fin

primes = calcPrimes((10**4)+5)
count = [0]*((10**4)+5)

# mark possibility for each pair
for i in primes:
	for j in primes:
		if (i+(2*j)) < len(count):
			count[(i+(2*j))] += 1

n = int(input())
for _ in range(n):
	print(count[int(input())])
