def swap(array,indexOne,indexTwo):
	temp = array[indexOne]
	array[indexOne] = array[indexTwo]
	array[indexTwo] = temp
def quickSort(array,l,r):
	pivot = l+(r-l)//2
	swap(array, pivot, r)
	pivot = r
	r-=1
	while(l<r):
		print array
		while(array[l] >= array[pivot] and l<r):
			l += 1
		while(array[r]<array[pivot] and r>l):
			r += 1
		swap(array, l, r)
	swap(array, l, pivot)
	quickSort(array, 0,l-1)
	quickSort(array, l+1, pivot)
	return array
array = [5,4,3,2,1]
print quickSort(array,0,len(array)-1)
