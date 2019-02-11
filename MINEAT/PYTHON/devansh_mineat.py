t=int(raw_input())
for i in range(0,t):
  n,h=map(int,raw_input().split())
  piles=list(map(int,raw_input().split()))
  piles.sort()

  
  
  l=1
  r=piles[n-1]
  
  final=None
  if(n==h):
    # in case hours is equal to piles
    final=r
  else:
    # binary search  for value of k
    while(l<r):
      mid=l+(r-l)//2
      # print(l,r,mid)
      flag=0
      counter=0
      for j in range(0,n):
        # split the values using k and add them to counter
        slots=piles[j]//mid
        if(piles[j]%mid!=0):
          slots+=1
        counter+=slots
        # if the lmit exceeds then break as this is not the k we want 
        if(counter>(h)):
        
          flag=1
          break

      if(flag==1):
        l=mid+1
      else:
        r=mid
      if(l==r):
        final=r
        break
  print(final)
  

