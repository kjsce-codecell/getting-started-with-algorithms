# Number of coins required for 'n' levels
def coinsReq(n):
	return n*(n+1)/2

#Binary search between ul and ll for optimal number of levels
def solve(coin):
	#set ll and ul
	ll = 1
	ul = 10**5
	#while ll is strictly less than ul
	while(ul>=ll):
		# get mid element
		mid = (ll+ul)//2
		# check where to move next
		if coinsReq(mid) > coin:
			# set ul
			ul = mid-1
		else:
			# set ll
			ll = mid+1
	print(ul)

n = int(input())
for _ in range(n):
	solve(int(input()))