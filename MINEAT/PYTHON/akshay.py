def predicate(k, h, piles):
    '''
    Returns True or False. Whether this value of k is enough to finish the bananas in time.
    '''

    nHours = 0
    for e in piles:
        nHours += e//k + (1 if e % k else 0)
    if nHours <= h:
        return True
    return False


t = int(input())
for __ in range(t):
    n, h = map(int, input().split())
    piles = list(map(int, input().split()))
    lo = 0
    hi = max(piles)
    while lo<hi:
        mid = (lo+hi)//2
        if predicate(mid, h, piles):
            hi = mid
        else:
            lo = mid+1
    print(lo)
