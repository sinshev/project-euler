# Problem 5
def multiplies(n):
	a = [i for i in xrange(11,21) if n%i==0]
	return a

def smallest_multiple():
	# primes product - 90 (number will ends with 00)
	primes = 2*3*5*7*11*13*17*19-90
	for i in xrange(primes,primes**2, 40):
		if len(multiplies(i))==10:
			print i
			return
smallest_multiple()