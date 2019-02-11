import math
t=int(input())
for i in range(0,t):
  n=int(input())
# answer is the positive root of n(n+1)/2=input
  sqr=math.sqrt(1+(8*n))
  root=sqr-1
  print(int(root//2))

