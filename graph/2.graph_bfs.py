###################################
#								  #
#		Author : Dhananjay		  #
#				 IIT Gandhinagar  #
#								  #
###################################

# BFS implementation - 		O(V+E)

from collections import deque, defaultdict
INF = 1000000000

def bfs(u):
	q = deque()
	dist = [INF] * V
	
	q.append(u)
	dist[u] = 0
	while q:
		u = q.popleft()
		print(u, end = " ")
		for v, w in AdjList[u]:
			if dist[v] == INF:
				q.append(v)
				dist[v] = dist[u] + 1

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
bfs(0)