fh = open("QuickSort.txt").read()
A = fh.split()
A =[int(x) for x in A] #Do not forget to change string into int

count = 0
def quick_sort(A,p,r):
	if p<r:
		q = partition(A,p,r)
		quick_sort(A,p,q-1)
		quick_sort(A,q+1,r)

def partition(A,p,r):
	med = A[p+(r-p)//2]
	first = A[p]
	end = A[r]
	templst = [(med,p+(r-p)//2),(first,p),(end,r)]
	templst.sort()
	x = templst[1][0]
	ind = templst[1][1]	
	#exchange the pivot element with the first element
	temp = A[ind]
	A[ind] = A[p]
	A[p] = temp
	i = p+1
	global count
	for j in xrange(p+1,r+1):
		count += 1
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