###################################
#								  #
#		Author : Dhananjay		  #
#				 IIT Gandhinagar  #
#								  #
###################################

# Check whether graph is bipartite or not		- 		O(V+E)

from collections import defaultdict, deque
INF = 10000000

def check_bipartite(u):
	isBipartite = True
	q = deque()										# for bfs
	q.append(u)
	colour[u] = 0									# used two colours - 0, 1 to mark vertices in graph
	
	while q and isBipartite:
		u = q.popleft()
		for v,w in AdjList[u]:
			if colour[v] == INF:					# unvisited vertex 'v'
				colour[v] = 1 - colour[u]
				q.append(v)
			elif colour[v] == colour[u]:			# visited virtex 'v' with same colour as 'u'
				isBipartite = False
				break
	return isBipartite
	

AdjList = defaultdict(list)
# Graph for which we will create AdjList. This is bipartite graph. You can add edge 0 --> 2 to make it non bipartite graph.
#
#          5
#      0 ----- 1
#            /
#		    /
#          / 2
#         / 
#        /  2
#      2 ----- 3
#        \
#         \
#          \ 7
#           \
#            \
#      5 ----- 4
#          8
AdjList = {0 : [[1,5]],
		   1 : [[0,5],[2,2]],
		   2 : [[1,2],[3,2],[4,7]],
		   3 : [[2,2]],
		   4 : [[2,7],[5,8]],
		   5 : [[4,8]]}
V = len(AdjList)
colour = [INF] * V

if check_bipartite(0):
	print("Given graph is bipartite")
else:
	print("Given graph is NOT bipartite")