# Python code for finding count
# of string in a given 2D
# character array.

# utility function to search
# complete string from any
# given index of 2d array
def internalSearch(ii, needle, row, col, hay,
					row_max, col_max):
	
	found = 0
	if (row >= 0 and row <= row_max and
		col >= 0 and col <= col_max and
		needle[ii] == hay[row][col]):
		match = needle[ii]
		ii += 1
		hay[row][col] = 0
		if (ii == len(needle)):
			found = 1
		else:
			
			# through Backtrack searching
			# in every directions
			found += internalSearch(ii, needle, row,
							col + 1, hay, row_max, col_max)
			found += internalSearch(ii, needle, row,
							col - 1, hay, row_max, col_max)
			found += internalSearch(ii, needle, row + 1,
							col, hay, row_max, col_max)
			found += internalSearch(ii, needle, row - 1,
							col, hay, row_max, col_max)
		hay[row][col] = match
	return found

# Function to search the string in 2d array
def searchString(needle, row, col,strr,
				row_count, col_count):
	found = 0
	for r in range(row_count):
		for c in range(col_count):
			found += internalSearch(0, needle, r, c,
						strr, row_count - 1, col_count - 1)
			
	return found

# Driver code

needle = "MAGIC"
inputt = ["BBABBM","CBMBBA","IBABBG",
			"GOZBBI","ABBBBC","MCIGAM"]

strr = [0] * len(inputt)

for i in range(len(inputt)):
	strr[i] = list(inputt[i])
	
print("count: ", searchString(needle, 0, 0, strr,
						len(strr), len(strr[0])))

# This code is contributed by SHUBHAMSINGH10
