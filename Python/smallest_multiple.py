# Problem 5
def smallest_multiple(n):
	a = [i for i in xrange(11,21) if n%i==0]
	return a

def bla():
	for i in xrange(300,100000000, 40):
		if len(smallest_multiple(i))==10:
			print i
			return
bla()
# print smallest_multiple(116396280)
# print len(smallest_multiple(116396280))
# a = [i for i in xrange(11,21)]
# print a
# print len(a)