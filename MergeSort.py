
def mergeSort(list):
	if (0<(len(list)-1)):
		m=(len(list)-2)/2
		list1 = list[:len(list)//2]
		list2 = list[len(list)//2:]
	mergeSort(list1)
	mergeSort(list2)


mergeSort([1,2,3,4,5,6])
