
from heapq import heappush, heappop
from collections import defaultdict

def mst_prim():
	minHeap = []
	taken = [0] * V
	mst_cost = 0
	
	def process(u):
		taken[u] = 1
		for v,w in AdjList[u]:
			if not taken[v]:
				heappush(minHeap, [w,v])
	process(0)
	while minHeap:
		w,v = heappop(minHeap)
		if not taken[v]:
			mst_cost += w
			process(v)
	return mst_cost

AdjList = defaultdict(list)
# Graph for which we will create AdjList
#
#			    1
#             /  \
#           4/    \2
#           /   4  \
#          0 ------ 2
#          |\      /
#          | \6   /8
#          |  \  /
#         6|   3
#          |  / 
#          | /9
#          |/        
#          4
AdjList = {0 : [[1,4], [2,4], [3,6], [4,6]],
		   1 : [[0,4], [2,2]],
		   2 : [[1,2], [3,8]],
		   3 : [[0,6], [2,8], [4,9]],
		   4 : [[0,6], [3,9]]}
V = len(AdjList)
print("MST cost : " + str(mst_prim()))