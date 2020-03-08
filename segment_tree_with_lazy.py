###################################
#								  #
#		Author : Dhananjay		  #
#				 IIT Gandhinagar  #
#								  #
###################################

# Segment Tree implementation with lazy propagation. The supported operations are:
#			- Range minimum query, 	O(log(n))
#			- Range update, 		O(log(n))

class SegmentTree:
	def __init__(self, arr):
		self.n = len(arr)
		self.A = arr[:]
		self.st = [0 for _ in range(4 * self.n)]
		self.lazy = [-1 for _ in range(4 * self.n)]
		self.build(1, 0, self.n - 1)
		
	def l(self, p):											# return left child of node 'p'
		return p << 1
		
	def r(self, p):											# return right child of node 'p'
		return (p << 1) + 1
		
	def conquer(self, a, b):								# this function obtains/conquers the result for current node given result of left child(here 'a') and result of right child(here 'b'). This function will be used in RMQ function.
		if a == -1:											# if left child value is invalid(-1 represents invalid), return right child value. This '-1' corresponds to return value of RMQ_() for inavlid case.
			return b
		if b == -1:											# if right child value is invalid(-1 represents invalid), return left child value
			return a
		return min(a,b)										# RMQ - if both children are valid, return minimum of them
															# Note : it is not possible that both the children are invalid because we are calling 'conquer' function for non leaf nodes of segment tree.
		
	def propagate(self, p, L, R):							# this propagates value from 'p'th node of lazy tree to corresponding segment tree node and it's left,right childrens. Also, clears the 'p'tn lazy node after propagation of the value.
		if self.lazy[p] != -1:
			self.st[p] = self.lazy[p]
			if L != R:										# if non-leaf node of segment tree, update it's children
				self.lazy[self.l(p)] = self.lazy[self.r(p)] = self.lazy[p]
			else:
				self.A[L] = self.lazy[p]					# if leaf node of segment tree, update copy of array 
			self.lazy[p] = -1
		
	def build(self, p , L, R):								# build node 'p' of segment tree which has range [L,R] associated with it.
		if L == R:											# leaf node of segment tree
			self.st[p] = self.A[L]
		else:
			m = (L + R) >> 1
			self.build(self.l(p), L,	m)
			self.build(self.r(p), m+1,	R)
			self.st[p] = self.conquer(self.st[self.l(p)], self.st[self.r(p)])
	
	def update_(self, p, L, R, i, j, val):
		if (i>R) or (j<L):									# [L R] .. [i j]    or     [i j] .. [L R] 
			return -1
		if (L>=i) and (R<=j):								# i .. [L R] .. j
			self.lazy[p] = val								# if segment found, we update result in lazy tree
			self.propagate(p, L, R)							# we propagate this updated result only to it's child (not whole segment tree)
		else:
			m = (L + R) >> 1
			self.update_(self.l(p), L	, m, i, j, val)		# update leftsubtree
			self.update_(self.r(p), m+1	, R, i, j, val)		# update rightsubtree
			
			lsubtree 	= self.lazy[self.l(p)] if self.lazy[self.l(p)]!= -1 else self.st[self.l(p)]				# get result for lsubtree from lazy tree if present otherwise from segment tree. NOTE : this ensures we are accounting updated results.
			rsubtree 	= self.lazy[self.r(p)] if self.lazy[self.r(p)]!= -1 else self.st[self.r(p)]				# get result for rsubtree from lazy tree if present otherwise from segment tree. NOTE : this ensures we are accounting updated results.
			self.st[p] 	= self.st[self.l(p)] if (lsubtree <= rsubtree) else self.st[self.r(p)]					# update the segment tree
		
	def update(self, i, j, val):							# wrapper function for update
		self.update_(1, 0, self.n - 1, i, j, val)
		
	def RMQ_(self, p, L, R, i, j):							# we are at node 'p' of segment tree which has range[L,R] associated with it and we need to find answer for range[i,j]
		self.propagate(p, L, R)								# we propagate result only on demand : lazy propagation
		if (i>R) or (j<L):									# [L R] .. [i j]    or     [i j] .. [L R] 
			return -1
		if (L>=i) and (R<=j):								# i .. [L R] .. j
			return self.st[p]
		m = (L + R) >> 1
		return self.conquer(self.RMQ_(self.l(p), L,		m,	i, j),
							self.RMQ_(self.r(p), m+1,	R,	i, j))
		
	def RMQ(self, i, j):									# wrapper function for RMQ
		return self.RMQ_(1, 0, self.n - 1, i, j)
		
lst = [18, 17, 13, 19, 15, 11, 20, 99, 2]
seg_tree = SegmentTree(lst)
print(seg_tree.RMQ(0,8))	# 2
print(seg_tree.RMQ(1,3))	# 13
print(seg_tree.RMQ(4,7))	# 11
print(seg_tree.RMQ(3,4))	# 15
seg_tree.update(7,7,1)
# lst = [18, 17, 13, 19, 15, 11, 20, 1, 2]
print(seg_tree.RMQ(0,8))	# 1
print(seg_tree.RMQ(0,6))	# 11
print(seg_tree.RMQ(7,8))	# 1
seg_tree.update(0,3,30)
# lst = [30, 30, 30, 30, 15, 11, 20, 1, 2]
print(seg_tree.RMQ(1,3))	# 30
print(seg_tree.RMQ(4,7))	# 1
print(seg_tree.RMQ(3,4))	# 15