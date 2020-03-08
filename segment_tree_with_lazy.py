#################################################
#						#
#		Author : Dhananjay		#
#			 IIT Gandhinagar  	#
#						#
#################################################

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
		
	def l(self, p):
		return p << 1
		
	def r(self, p):
		return (p << 1) + 1
		
	def conquer(self, a, b):
		if a == -1:
			return b
		if b == -1:
			return a
		return min(a,b)
		
	def propagate(self, p, L, R):
		if self.lazy[p] != -1:
			self.st[p] = self.lazy[p]
			if L != R:
				self.lazy[self.l(p)] = self.lazy[self.r(p)] = self.lazy[p]
			else:
				self.A[L] = self.lazy[p]
			self.lazy[p] = -1
		
	def build(self, p , L, R):
		if L == R:
			self.st[p] = self.A[L]
		else:
			m = (L + R) >> 1
			self.build(self.l(p), L,	m)
			self.build(self.r(p), m+1,	R)
			self.st[p] = self.conquer(self.st[self.l(p)], self.st[self.r(p)])
	
	def update_(self, p, L, R, i, j, val):
		if (i>R) or (j<L):
			return -1
		if (L>=i) and (R<=j):
			self.lazy[p] = val
			self.propagate(p, L, R)
		else:
			m = (L + R) >> 1
			self.update_(self.l(p), L	, m, i, j, val)
			self.update_(self.r(p), m+1	, R, i, j, val)
			
			lsubtree 	= self.lazy[self.l(p)] if self.lazy[self.l(p)]!= -1 else self.st[self.l(p)]
			rsubtree 	= self.lazy[self.r(p)] if self.lazy[self.r(p)]!= -1 else self.st[self.r(p)]
			self.st[p] 	= self.st[self.l(p)] if (lsubtree <= rsubtree) else self.st[self.r(p)]
		
	def update(self, i, j, val):
		self.update_(1, 0, self.n - 1, i, j, val)
		
	def RMQ_(self, p, L, R, i, j):
		self.propagate(p, L, R)
		if (i>R) or (j<L):
			return -1
		if (L>=i) and (R<=j):
			return self.st[p]
		m = (L + R) >> 1
		return self.conquer(self.RMQ_(self.l(p), L,		m,	i, j),
							self.RMQ_(self.r(p), m+1,	R,	i, j))
		
	def RMQ(self, i, j):
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
