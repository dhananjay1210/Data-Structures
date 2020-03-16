###################################
#								  #
#		Author : Dhananjay		  #
#				 IIT Gandhinagar  #
#								  #
###################################

# DFS implementation - 		O(V+E)

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
#         |/
#         3
AdjList = {0 : [[1,7]],
		   1 : [[0,7],[3,8],[2,5]],
		   2 : [[1,5],[3,5],[4,9]],
		   3 : [[1,8],[2,5]],
		   4 : [[2,9],[5,1]],
		   5 : [[4,1]]}
V = len(AdjList)
dfs_num = [UNVISITED] * V
dfs(0)