# Problem 5
def get_multiplies(n, multiplies):
	a = [i for i in xrange(1,multiplies+1) if n%i==0]
	return a

def smallest_multiple(multiplies):
	for i in xrange(2,multiplies**10, 2):
		if len(get_multiplies(i, multiplies))==multiplies:
			return i

# print smallest_multiple(20)
