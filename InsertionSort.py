test = [4,1,5,0,10,23,9,23,0,120]
for n in range(1,len(test)):
	selector = test[n]
	for f in range(n,0,-1):
		if (selector<test[f-1]):
			print "swapped", f-1, n
			buf = test[f-1]
			test[f-1]=selector
			test[f]=buf
print test

