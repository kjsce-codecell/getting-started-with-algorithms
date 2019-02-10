t = int(input())
for i in range(t):
    n=int(input())
    l=0
    h=100000   
    while l<=h:
        mid =(l+h)//2
        r= (mid*(mid+1))//2
        if r>n:
            h=mid - 1
        else:
            ht=mid
            l=mid+1
    print(ht)
