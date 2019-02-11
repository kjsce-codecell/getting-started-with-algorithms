n=10000
result=[]
prime=[True for i in range(n+1)]
result=[0 for i in range(0,100000000)]
ls=[]
#calculate list of prime number before hand and directly query inside main loop
for j in range(2,n):    
  if(prime[j]==True):
    ls.append(j)
    for k in range(j*j,n+1,j):
    
      prime[k]=False
  j+=1
for p in ls:
  for q in ls:
  
    result[p+2*q]+=1



t=int(input())
for i in range(0,t):
  num=int(input())
  print(result[num])

