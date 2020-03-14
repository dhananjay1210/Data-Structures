###################################
#								  #
#		Author : Dhananjay		  #
#				 IIT Gandhinagar  #
#								  #
###################################

# Fenwick Tree implementation. The supported operations are:
#			- point query, 		O(log(n))
#			- range update, 	O(log(n))

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
	
	def RSQ(self, i):									# returns value of freq array at index i.
		sm = 0
		while i:
			sm += self.ft[i]
			i -= self.LSOne(i)
		return sm
	
	def update_(self, i, val):							# adds val to index i of freq array
		while i <= self.n:
			self.ft[i] += val
			i += self.LSOne(i)
			
	def update(self, i, j, val):						# adds val from index i to index j of freq array
		self.update_(i, val)
		self.update_(j+1, -val)
	

freq = [0]*10	# NOTE : Treat this as 1-based index array
ft = FenwickTree(freq)			

ft.update(5, 7, 3)
# freq = [0, 0, 0, 0, 3, 3, 3, 0, 0, 0]
print(ft.RSQ(6))		# 3
print(ft.RSQ(7))		# 3
print(ft.RSQ(8))		# 0
print(ft.RSQ(3))		# 0

ft.update(7, 10, 2)
# freq = [0, 0, 0, 0, 3, 3, 5, 2, 2, 2]
print(ft.RSQ(6))		# 3
print(ft.RSQ(7))		# 5
print(ft.RSQ(8))		# 2
print(ft.RSQ(3))		# 0
