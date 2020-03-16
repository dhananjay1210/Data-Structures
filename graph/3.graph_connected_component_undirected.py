###################################
#								  #
#		Author : Dhananjay		  #
#				 IIT Gandhinagar  #
#								  #
###################################

# Connected components in UNDIRECTED graph  - 		O(V+E)

from collections import defaultdict
UNVISITED = 0
EXPLORED = 1
VISITED = 2

def dfs(u):
	print(u, end = " ")
	dfs_num[u] = VISITED
	for v,w in AdjList[u]:
		if dfs_num[v] == UNVISITED:
			dfs(v)
	
AdjList = defaultdict(list)
# Graph for which we will create AdjList.
#
#      7     5     9     1
#	0 --- 1 --- 2 --- 4 --- 5
#		  |   /
#		 8|  / 5
#		  | /
#         |/       3     1
#         3     6 --- 7 --- 8
AdjList = {0 : [[1,7]],
		   1 : [[0,7],[3,8],[2,5]],
		   2 : [[1,5],[3,5],[4,9]],
		   3 : [[1,8],[2,5]],
		   4 : [[2,9],[5,1]],
		   5 : [[4,1]],
		   6 : [[7,3]],
		   7 : [[6,3],[8,1]],
		   8 : [[7,1]]}
V = len(AdjList)
dfs_num = [UNVISITED] * V
CC = 1
for u in range(V):
	if dfs_num[u] == UNVISITED:
		print("CC", CC, ": ", end = "" )
		dfs(u)
		print()
		CC += 1