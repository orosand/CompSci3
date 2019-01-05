import numpy as np
# testing array
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print x
# temp array made empty, each axis is the size of the opposite axis as the x array
temp = np.empty([x.shape[1],x.shape[0]])
# for loop for the size of one axis
for n in range(0,x.shape[1]):
	# counts backwards for the x array so that it is rotate from the center, otherwise it would rotate from the upper left corner, so not true rotation
	temp[n,:] = x[:,-n-1]
# same for loop for other axis
for n in range(0,x.shape[0]):
	temp[:,n] = x[-n-1,:]
x = temp
print x

