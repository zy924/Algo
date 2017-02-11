#Count inversion

##input 
fh = open("IntegerArray.txt")
strs = fh.read()
a = strs.split()
aint = [int(x) for x in a]
inputs = (aint,0)
count = 0
def merge_count(x,y):
	nx = len(x[0])
	ny = len(y[0])
	newlst = []
	i=0
	j=0
	global count
	x[0].append(1e10)
	y[0].append(1e10)
	for k in xrange(nx+ny):
		if x[0][i]<=y[0][j]:
			newlst.append(x[0][i])
			i += 1
		else:
			newlst.append(y[0][j])
			count += len(x[0][i:-1])
			j += 1
	return (newlst,count)

def mergesort((a,num)):
	n = len(a)
	if n > 1:
		return merge_count(mergesort((a[:n//2],num)),mergesort((a[n//2:],num)))
	else:
		return (a,0)

if __name__ == "__main__":
	#assert mergesort([1])==[1],"False Algo when input size is 1"
	#assert mergesort([1,3,5])==[1,3,5],"False Algo for best case"
	#assert mergesort([5,3,1])==[1,3,5],"False Algo for worst case"
	print mergesort(inputs)

