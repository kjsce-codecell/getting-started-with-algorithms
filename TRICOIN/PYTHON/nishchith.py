t = int(input())
for _ in range(t):
    n = int(input())    # available coins

    left = 1
    right = 10**5   
    ans = 0

    while left <= right:
        mid = left + ( right - left )//2
        
        required = mid*(mid + 1)//2     # required gold coins
        if required > n:
            right = mid - 1
        else:
            ans = mid 
            left = mid + 1

    print(ans)
