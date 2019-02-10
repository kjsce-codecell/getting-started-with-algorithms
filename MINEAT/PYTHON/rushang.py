for _ in range(int(input())): # Iterating over all testcases
    n,h = map(int,input().split()) 
    a = list(map(int,input().split()))
    min_banana = 1
    banana = max_banana = max(a)
    # Applying binary search to find #bananastobeeaten in closest to h hours
    while min_banana<=max_banana:
        x = (min_banana+max_banana)//2
        hours = 0
        # calculating the #hours required if 'x' banana are eaten per hour
        for ban in a: 
            hours += (ban - 1)//x + 1
        if hours <= h: # eat less bananas so that it takes more time
            max_banana = x - 1
            banana = min(banana, x) 
        else: # eat more bananas 
            min_banana = x + 1
    print(banana)
