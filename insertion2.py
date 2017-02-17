"""
Applied Insertion Sort
Everytime you insert an element into a sorted array, you should print the array
For example:
Input:
1 4 5 2 3
OutPut:
1 4 5 2 3
1 4 5 2 3
1 2 4 5 3
1 2 3 4 5
"""

#Default Input
arr = [1,4,5,2,3]

#Insert an element into a sorted array
def insertion(ar,j):
    m = len(ar[:j+1])
    e = ar[m-1]
    for i in xrange(m-2,-1,-1):
        if ar[i]<=e:
            ar[i+1]=e
            break
        else:
            ar[i+1]=ar[i]
    if e<=ar[0]:
        ar[0]=e
    return 

#Insertion sort
def insertionSort(ar):
    n = len(ar)
    for i in xrange(1,n):
        insertion(ar,i)
        print " ".join(map(str,ar))
    return

if __name__ == "__main__":
	insertionSort(arr)