###################################
#								  #
#		Author : Dhananjay		  #
#				 IIT Gandhinagar  #
#								  #
###################################

# Finding articulation point and bridges
# Extension of dfs 					 - 		O(V+E)

from collections import defaultdict
UNVISITED = 0
EXPLORED = 1
VISITED = 2

def articulation_points_and_bridges(u):
	global dfsNumber, dfsRoot, rootChildren
	dfs_num[u] = dfs_low[u] = dfsNumber
	dfsNumber += 1
	for v,w in AdjList[u]:
		if dfs_num[v] == UNVISITED:
			dfs_parent[v] = u
			if u == dfsRoot:
				rootChildren += 1
			articulation_points_and_bridges(v)
			
			if dfs_low[v] >= dfs_low[u]:
				articulation_vertex[u] = True
			if dfs_low[v] > dfs_low[u]:
				print("Edge",u,"-->",v,"is a bridge")
				
			dfs_low[u] = min(dfs_low[u], dfs_low[v])
		elif v != dfs_parent[u]:
			dfs_low[u] = min(dfs_low[u], dfs_num[v])

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
dfs_low = [0] * V
dfs_parent = [0] * V
articulation_vertex = [False] * V
dfsNumber = 0

for i in range(V):
	if dfs_num[i] == UNVISITED:
		dfsRoot = i
		rootChildren = 0
		articulation_points_and_bridges(i)
		articulation_vertex[i] = (rootChildren > 1)

print("Articulation vertices : ")
for i in range(V):
	if articulation_vertex[i]:
		print(i)