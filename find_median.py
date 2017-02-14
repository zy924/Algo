"""
Find Median of an array, the element is dinstinct
Define: 
	if the length of the array is odd, the median is (n+1)/2
	else the median is n/2
"""
B = [1,2,3,4,5,6,7,8,9,10,11,12]

def find_median(A,k):
	n = len(A)
	pivot = A[n//2]
	A_minus = [x for x in A if x<pivot]
	A_plus = [x for x in A if x>pivot]
	if len(A_minus)-1==k-1:
		print A[n//2]
		return
	elif len(A_minus)-1>=k:
		find_median(A_minus,k)
	elif len(A_minus)-1<k-1:
		find_median(A_plus,k-len(A_minus)-1)

if __name__ == "__main__":
	#assert find_median([5,2,1,3,4])==3, "Odd input is false"
	#assert find_median([4,3,1,2])==2, "Even input is false"
	if len(B)%2==0:
		find_median(B,len(B)/2-1)
	else:
		find_median(B,(len(B)+1)/2-1)



