def sieve(n):
    #Create list of numbers from 0 to n
    #True denotes prime, false not prime 
    l=[True for i in range(n+1)]
    #Start with 2
    p=2
    while(p*p<n):
        #and cross off all it's multiples 
        if l[p]: 
            for i in range(p*p, n+1, p): 
                l[i] = False
        #increment p to next value 
        p+=1
    #adding all prime numbers to a list and returning it 
    primes=[]
    for i in range(2,n):
        if l[i]:
            primes.append(i)
    return primes

sums=[0]*(10001)
p=sieve(10001)

#calculating all possible sums as per question and storing the count of each
for i in p:
    for j in p:
        if i+(2*j) <= 10000:
            sums[i+(2*j)]+=1

#input number of test cases
t=int(input())
while t:
    n=int(input())
    #input number and check if it is in the pre-built list
    print(sums[n])
    t-=1
