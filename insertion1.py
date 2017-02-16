"""
Insert a number into a sorted array, the number will in the rightmost cell.
Print the array every time a number is shifted.
For example:
Input:
2 3 4 1
Output:
2 3 4 4
2 3 3 4
2 2 3 4
1 2 3 4
"""
#input
A = [2,3,4,5,1]

def insertion1(ar):
	m = len(ar)
	e = ar[-1]
	for i in xrange(m-2,-1,-1):
		if ar[i]<=e:
			ar[i+1]=e
			print " ".join(map(str,ar))
			break
		else:
			ar[i+1]=ar[i]
			print " ".join(map(str,ar))
	if e<ar[0]: #Be careful when you down to the 0 index
		ar[0]=e
		print " ".join(map(str,ar))
	return 

if __name__ == "__main__":
	insertion1(A)