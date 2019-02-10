import math

for _ in range(int(input())):
    n, h = map(int, input().split(' '))
    b = list(map(int, input().split(' ')))
    #b.sort()
    mi = 1
    ma = max(b)
    ans = ma + 1
    while mi <= ma: #binary search
        mid = (mi + ma)//2
        count = 0
        #calculate no. of hours required for K=i 
        for i in b:
            count += math.ceil(i / mid)
        
        #if count is in acceptable range set ans = minimum of 'mid' or the prev iter 'ans' 
        if count <= h:
            ans = min(mid, ans)
        
        #binary search 
        if count <= h:
            ma = mid - 1
        else:
            mi = mid + 1