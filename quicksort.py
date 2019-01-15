from random import randint
def quickSort(a,l,r):
	if(l<r):
		pivot = partition(a,l,r)
		quickSort(a,l,pivot-1)
		quickSort(a,pivot+1,r)
	return a
array = [1,5,23,1,5,3,4,2,3,45,75,23,70,100,10,234,123,34,12]
def partition(a, left, right):
		pivotIndex = randint(left,right)
		p=a[pivotIndex]
		a[right],a[pivotIndex] = a[pivotIndex], a[right]
		right -= 1
		minIndex = left
		for i in range(left,right+1):
			if(a[i]<=p):
				a[i],a[minIndex] = a[minIndex], a[i]
				minIndex +=1
		a[minIndex],a[right+1] = a[right+1],a[minIndex]
		return minIndex


print quickSort(array,0,len(array)-1)






