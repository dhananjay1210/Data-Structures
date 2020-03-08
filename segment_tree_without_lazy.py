###################################
#								  #
#		Author : Dhananjay		  #
#				 IIT Gandhinagar  #
#								  #
###################################

# Segment Tree implementation without lazy propagation. The supported operations are:
#			- Range minimum query, O(log(n))
#			- Point update, O(log(n))

class SegmentTree:
	def __init__(self, arr):
		self.n = len(arr)
		self.A = arr[:]
		self.st = [0 for _ in range(4* self.n)]
		self.build(1, 0, self.n - 1)
		
	def l(self, p):										# return left child of node 'p'
		return p << 1
	
	def r(self, p):										# return right child of node 'p'
		return (p << 1) + 1
		
	def conquer(self, a, b):							# this function obtains/conquers the result for current node given result of left child(here 'a') and result of right child(here 'b'). This function will be used in RMQ function.
		if a == -1:										# if left child value is invalid(-1 represents invalid), return right child value. This '-1' corresponds to return value of RMQ_() for inavlid case.
			return b
		if b == -1:										# if right child value is invalid(-1 represents invalid), return left child value
			return a
		return min(a,b)									# RMQ - if both children are valid, return minimum of them
														# Note : it is not possible that both the children are invalid because we are calling 'conquer' function for non leaf nodes of segment tree.
												
	def build(self, p, L, R):							# build node 'p' of segment tree which has range [L,R] associated with it.
		if L == R:										# leaf node of segment tree
			self.st[p] = self.A[L]
		else:
			m = (L + R) >> 1
			self.build(self.l(p)	, L		, m)
			self.build(self.r(p)	, m+1	, R)
			self.st[p] = self.conquer(self.st[self.l(p)], self.st[self.r(p)])
	
	def RMQ_(self, p, L, R, i, j):						# we are at node 'p' of segment tree which has range[L,R] associated with it and we need to find answer for range[i,j]
		if (i>R) or (j<L):								# [L R] .. [i j]    or     [i j] .. [L R] 
			return -1
		if (L>=i and R<=j):								# i .. [L R] .. j
			return self.st[p]
		m = (L + R) >> 1
		return self.conquer(self.RMQ_(self.l(p),	L,	 m,	i,	j),
							self.RMQ_(self.r(p), 	m+1, R,	i,	j))
					   
	def RMQ(self, i, j):
		return self.RMQ_(1, 0, self.n - 1, i, j)
		
	def update_(self, p, L, R, i, val):					# we are at node 'p' of segment tree which has range[L,R] associated with it and we need to to update A[i] = val and propagate result in segment tree from leaf(A[i]) to root.
		if (i>R) or (i<L):								# [L R] .. [i j]    or     [i j] .. [L R]
			return 
		if L == R == i:									# we reach the leaf node of segment tree
			self.st[p] = val							# update this leaf node(i.e. 'p'th node which stores actual array value)
			self.A[i] = val								# update temporary copy of array
			return
		m = (L + R) >> 1
		self.update_(self.l(p),	L,	 m,	i,	val)		# update the left and right child of 'p'th node and then update 'p'th node of segment tree
		self.update_(self.r(p), m+1, R,	i,	val)
		self.st[p] = self.conquer(self.st[self.l(p)], self.st[self.r(p)])
	
	def update(self, i , val):
		self.update_(1, 0, self.n - 1, i, val)
			

lst = [18, 17, 13, 19, 15, 11, 20, 99, 2]
seg_tree = SegmentTree(lst)
print(seg_tree.RMQ(0,8))	# 2
print(seg_tree.RMQ(1,3))	# 13
print(seg_tree.RMQ(4,7))	# 11
print(seg_tree.RMQ(3,4))	# 15
seg_tree.update(7,1)
# lst = [18, 17, 13, 19, 15, 11, 20, 1, 2]
print(seg_tree.RMQ(0,8))	# 1
print(seg_tree.RMQ(0,6))	# 11
print(seg_tree.RMQ(7,8))	# 1
