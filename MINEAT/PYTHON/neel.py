# calculate number of hours to eat all bananas
def cost(piles,limit):
	cost = 0
	for pile in piles:
		cost += pile//limit
		if pile%limit:
			cost += 1
	return cost

def solve(hours,piles):
	ll = 1
	ul = max(piles)
	ans = 10**9
	# do untill last iteration, even after equal
	while(ul>=ll):
		# assign middle
		mid = (ll+ul)//2

		# check against current ans, if lower change
		if cost(piles,mid) <= hours:
			ans = min(mid,ans)

		# need to eat more bananas, for lesser cost
		if cost(piles,mid) > hours:
			ll = mid + 1
		else:
			ul = mid - 1
	print(ans)

n = int(input())
for _ in range(n):
	n,h = map(int, input().split())
	piles = list(map(int, input().split()))
	solve(h,piles)