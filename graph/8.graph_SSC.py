###################################
#								  #
#		Author : Dhananjay		  #
#				 IIT Gandhinagar  #
#								  #
###################################

# Finding strongly connected components(SSC) in directed graph
# Extension of dfs 					 - 		O(V+E)

from collections import defaultdict
UNVISITED = 0
EXPLORED = 1
VISITED = 2

def SSC(u):
	global dfsNumber, sscNumber
	dfs_low[u] = dfs_num[u] = dfsNumber
	dfsNumber += 1
	visited[u] = VISITED
	stc.append(u)
	
	for v,w in AdjList[u]:
		if dfs_num[v] == UNVISITED:
			SSC(v)
		if visited[v]:
			dfs_low[u] = min(dfs_low[u], dfs_low[v])
	
	if dfs_low[u] == dfs_num[u]:
		sscNumber += 1 
		print("SSC", sscNumber,":", end = " ")
		while True:
			v = stc.pop()
			visited[v] = UNVISITED
			print(v, end = " ")
			if u == v:
				break
		print()


AdjList = defaultdict(list)
# Graph for which we will create AdjList.
#
#        7       5        9       1
#	0 ------> 1 ---> 2 ------> 4 ---> 5
#		      ^   /		       ^      |
#		     8|  / 5	      5|	  | 3
#		      | /		       |	  |
#             |v      	       |   3  v   
#             3     	       6 <--- 7
AdjList = {0 : [[1,7]],
		   1 : [[2,5]],
		   2 : [[3,5],[4,9]],
		   3 : [[1,8]],
		   4 : [[5,1]],
		   5 : [[7,3]],
		   6 : [[4,5]],
		   7 : [[6,3]]}
V = len(AdjList)
dfs_num = [UNVISITED]*V
dfs_low = [UNVISITED]*V
visited = [UNVISITED]*V
stc = []
dfsNumber = 0
sscNumber = 0

for i in range(V):
	if dfs_num[i] == UNVISITED:
		SSC(i)
