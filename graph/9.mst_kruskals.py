###################################
#								  #
#		Author : Dhananjay		  #
#				 IIT Gandhinagar  #
#								  #
###################################

# Finding MST of undirected graph		-	O(E*log(V))

class UnionFind:
	def __init__(self, V):
		self.uf = [i for i in range(V)]
		self.size = [1 for i in range(V)]
		
	def find(self, x):
		if self.uf[x] == x:
			return x
		else:
			root = self.find(self.uf[x])
			self.uf[x] = root
			return root

	def union(self, x, y):
		parent_x = self.find(x)
		parent_y = self.find(y)
		if parent_x != parent_y:
			if self.size[parent_x] <= self.size[parent_y]:
				self.uf[parent_x] = parent_y
				self.size[parent_y] += self.size[parent_x]
			else:
				self.uf[parent_y] = parent_x
				self.size[parent_x] += self.size[parent_y]

def mst_kruskal():
	EdgeList.sort(key = lambda x : (x[0], x[1][0], x[1][1]))	# sort on the basis of weight, in case of tie - sort 
	mst_cost = 0												# on the basis of staring point of edge, in case of 
	uf_ = UnionFind(V)											# tie - sort on the basis of ending point of the edge
	
	for w,[u,v] in EdgeList:
		if uf_.find(u) != uf_.find(v):
			mst_cost += w
			uf_.union(u,v)
	return mst_cost

V = 5
EdgeList = [[4, [0,1]],		# EdgeList[i][0] = weight of the edge,  EdgeList[i][0] and EdgeList[i][1] are 
			[4, [0,2]],		# end points of the edge
			[6, [0,3]],
			[6, [0,4]],
			[2, [2,1]],
			[8, [2,3]],
			[9, [3,4]]]
# Graph will look like this
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
print("MST cost : " + str(mst_kruskal()))