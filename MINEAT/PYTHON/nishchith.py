# Submission in PyPy
t = int(raw_input())
for _ in range(t):
    n_items, m_hours = map(int,raw_input().split())
    bag = list(map(int,raw_input().split()))
    
    if n_items == m_hours:
        # if number items in bag equals hours, lazy true
        print(max(bag))
    else:
        left = 1            # min pick K
        right = max(bag)    # max pick K
        ans = 10**9          # buffer to find min K

        # search 
        while left <= right :
            mid = left + (right - left)//2
            
            # current pick K = mid
            count = 0
            for i in range(n_items):
                count += bag[i]//mid
                count += 1 if ( bag[i]%mid ) != 0 else 0

            # if valid 
            if count <= m_hours:
                # pick minimum
                ans = min(mid, ans)
            if count > m_hours :
                left = mid + 1
            else : 
                right = mid - 1 
        
        print(ans)
