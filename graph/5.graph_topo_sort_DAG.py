###################################
#								  #
#		Author : Dhananjay		  #
#				 IIT Gandhinagar  #
#								  #
###################################

# Topological sort in DAG 
# Similar to dfs except addition of one line in dfs function 	- 		O(V+E)

from collections import defaultdict
UNVISITED = 0
EXPLORED = 1
VISITED = 2

def dfs(u):
	dfs_num[u] = VISITED
	for v,w in AdjList[u]:
		if dfs_num[v] == UNVISITED:
			dfs(v)
	stc.append(u)									# append to stack after performing dfs on all connected nodes
													# this ensures that all 'v' has been added before 'u' for each u --> v egde.
													# thus creating toposort in reverse order.
	
AdjList = defaultdict(list)
# Graph for which we will create AdjList.
#
#      7      5      9      1
#	0 ---> 1 ---> 2 ---> 4 ---> 5
#		   |   ^
#		  8|  / 5
#		   | /
#          v/       3       1
#          3     6 ---> 7 <--- 8
AdjList = {0 : [[1,7]],
		   1 : [[3,8],[2,5]],
		   2 : [[4,9]],
		   3 : [[2,5]],
		   4 : [[5,1]],
		   5 : [],
		   6 : [[7,3]],
		   7 : [],
		   8 : [[7,1]]}
stc = []
V = len(AdjList)
dfs_num = [UNVISITED]*V

for i in range(V):
	if dfs_num[i] == UNVISITED:
		dfs(i)

print(stc[::-1])					 				# stc has toposort in reverse order.