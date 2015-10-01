# Problem 6
def difference():
	a = sum([i*i for i in xrange(1,101)])
	b = sum([i for i in xrange(1,101)])**2
	print b - a

difference()