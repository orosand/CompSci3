
def mergeSort(list):
	if (len(list)==1):
		return list
	list1 = list[:len(list)//2]
	list2 = list[len(list)//2:]
	return merge(mergeSort(list1),mergeSort(list2))
def merge(list1,list2):
	indexOne = 0
	indexTwo = 0
	tempArray = []
	while indexOne<len(list1) and indexTwo<len(list2):
		if list1[indexOne]>list2[indexTwo]:
			tempArray.append(list1[indexOne])
			indexOne += 1
		else:
			tempArray.append(list2[indexTwo])
			indexTwo += 1
	while indexOne<len(list1):
		tempArray.append(list1[indexOne])
		indexOne += 1
	while indexTwo<len(list2):
		tempArray.append(list2[indexTwo])
		indexTwo += 1


	return tempArray
print mergeSort([1,2,45,1,2,5,5134314,314,1,23,436,])
