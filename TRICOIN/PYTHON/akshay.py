def predicate(h, n):
    '''
    Returns True if we can build a triangle of height h using n coins, else returns False
    '''
    return h*(h+1)//2 <= n

t = int(input())
for __ in range(t):
    n = int(input())
    # binary search for the greatest height which can be reached using n coins
    lo = 0
    hi = n
    while lo<hi:
        mid = lo + (hi-lo+1)//2  # round UP
        if predicate(mid, n):
            lo = mid
        else:
            hi = mid-1
    print(lo)