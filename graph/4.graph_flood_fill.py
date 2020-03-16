###################################
#								  #
#		Author : Dhananjay		  #
#				 IIT Gandhinagar  #
#								  #
###################################

# FloodFill implementation - Colouring connected component of the graph.
#
# Given a matrix representing land and water regions, in this implementation,
# I have coloured only one water region(mat[1][2]) and returned its size    - 			O(m * n)

dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]

def floodFill(mat, i, j, colour1, colour2):
	if i<0 or i>=m or j<0 or j>=n:									# invalid location
		return 0
	if mat[i][j] != colour1:										# not the water region  	 OR		 already visited water region(avoids cycle)
		return 0
	
	ans = 1
	mat[i][j] = colour2												# avoids cycle
	for dx_, dy_ in zip(dx,dy):										# explore neighborhood
		ans += floodFill(mat, i + dx_, j + dy_, colour1, colour2)	# dfs
	return ans
	
mat = [ ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
		['L', 'L', 'W', 'W', 'L', 'L', 'W', 'L', 'L'],
		['L', 'W', 'W', 'L', 'L', 'L', 'L', 'L', 'L'],
		['L', 'W', 'W', 'W', 'L', 'W', 'W', 'L', 'L'],
		['L', 'L', 'L', 'W', 'W', 'W', 'L', 'L', 'L'],
		['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
		['L', 'L', 'L', 'W', 'W', 'L', 'L', 'W', 'L'],
		['L', 'L', 'W', 'L', 'W', 'L', 'L', 'L', 'L'],
		['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']]
m,n = len(mat), len(mat[0])
size_of_component = floodFill(mat, 1, 2, 'W', '.')					# after colouring, I have replaced water region by '.'
print("Size of connected component is : ",size_of_component)
for rw in mat:
	print(rw)