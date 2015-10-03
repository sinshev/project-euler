# Problem 10

def is_prime(k):
	for i in xrange(2,k):
		if k%i==0:
			return False
	return True

def sum_of_primes(n):
	s = 2+3
	for i in xrange(4,n):
		if is_prime(i):
			s = s+i
			print s
	print s
			
# sum_of_primes(2000000)
# lst = [2*i-1 for i in xrange(2,1000000)]
# lst = (2*i-1 for i in xrange(2,1000000))
lst = [i for i in xrange(2,1000000,2)