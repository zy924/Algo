fh = open("QuickSort.txt").read()
A = fh.split()
A = [int(x) for x in A] #Do not forget to change the string into int

count = 0
def quick_sort(A,p,r):
	if p<r:
		q = partition(A,p,r)
		quick_sort(A,p,q-1)
		quick_sort(A,q+1,r)

def partition(A,p,r):
	x = A[r]
	#exchange the pivot element with the first element
	temp = A[r]
	A[r] = A[p]
	A[p] = temp
	i = p+1
	global count
	count += r-p
	for j in xrange(p+1,r+1):
		if A[j]<=x:
			temp = A[j]
			A[j] = A[i]
			A[i] = temp
			i +=1
	temp = A[i-1]
	A[i-1] = A[p]
	A[p] = temp
	return i-1

if __name__ == "__main__":
	quick_sort(A,0,len(A)-1)
	print A
	print count