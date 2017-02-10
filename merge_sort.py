##input 
a = [1,10,8,5,6,3,4,2,7,9,11,12,50]
from math import ceil
from math import floor
def merge(x,y):
	nx = len(x)
	ny = len(y)
	newlst = []
	i=0
	j=0
	x.append(10000)
	y.append(10000)
	for k in xrange(nx+ny):
		if x[i]<=y[j]:
			newlst.append(x[i])
			i += 1
		else:
			newlst.append(y[j])
			j += 1
	return newlst

def mergesort(a):
	n = len(a)
	if n > 1:
		return merge(mergesort(a[:n//2]),mergesort(a[n//2:]))
	else:
		return a

if __name__ == "__main__":
	assert mergesort([1])==[1],"False Algo when input size is 1"
	assert mergesort([1,3,5])==[1,3,5],"False Algo for best case"
	assert mergesort([5,3,1])==[1,3,5],"False Algo for worst case"
	print mergesort(a)

