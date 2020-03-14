###################################
#								  #
#		Author : Dhananjay		  #
#				 IIT Gandhinagar  #
#								  #
###################################

# Fenwick Tree implementation. The supported operations are:
#			- Range sum query, 		O(log(n))
#			- point update, 		O(log(n))

class FenwickTree:
	def __init__(self, freq):
		self.n = len(freq)
		self.A = freq[:]
		self.ft = [0 for _ in range(self.n + 1)]
		self.build(freq, self.ft)
		
	def LSOne(self, a):									# return least significant bit if 'a'
		return a & (-a)
	
	def build(self, freq, ft):							# O(n)
		for i in range(1, self.n + 1):
			self.ft[i] += freq[i-1]						# save current value if ft			
			if (i + self.LSOne(i)) <= self.n:				
				self.ft[i + self.LSOne(i)] += self.ft[i]# propagate current index(i) value to ONLY one next responsible index(say,j).
														# index i could be responsible for multiple further index. But, we only do one progation since 
														# all subsequent propagation will be carried out when we update ft[j].
	
	def RSQ_(self, i):									# returns sum of values of freq array from index 1 to index i.
		sm = 0
		while i:
			sm += self.ft[i]
			i -= self.LSOne(i)
		return sm
		
	def RSQ(self, i, j):								# returns sum of values of freq array from index i to index j.
		if i > 1:
			return self.RSQ_(j) - self.RSQ_(i-1)
		else:
			return self.RSQ_(j)
	
	def update(self, i, val):							# adds val to index i of freq array
		while i <= self.n:
			self.ft[i] += val
			i += self.LSOne(i)
	

freq = [0, 1, 0, 1, 2, 3, 2, 1, 1, 0]	# NOTE : Treat this as 1-based index array
										# This is frequecy array for arr = [2,4,5,6,6,6,7,7,8,9]
										# If we are given array 'arr' with length(arr) = m and arr[i] = [1 ... n], we can create freq array in O(m) and len(freq) will be equal to 'n'.
ft = FenwickTree(freq)			
print(ft.RSQ(1, 6))			# 7
print(ft.RSQ(1, 3))			# 1
print(ft.RSQ(4, 7))			# 8
print(ft.RSQ(1, 10))		# 11
ft.update(5, 3)
print(ft.RSQ(1, 10))		# 14
