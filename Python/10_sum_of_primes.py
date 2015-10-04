# Problem 10

def is_prime(k):
	for i in xrange(7,k,2):
		if k%i==0:
			return False
	return True

def sum_of_primes(n):
	s = 2+3+5 # first 3 primes
	lst = [i for i in xrange(7,n,2) if i%3!=0 and i%5!=0]
	for x in lst:
		if is_prime(x):
			s = s+x
	print s
			
# sum_of_primes(2000000) # takes approx. 10 minutes

def sum_of_primes_2(n):
    sieve = [True] * n
    s = 0
    current_prime = 2
    while current_prime < n:
        if sieve[current_prime]:
            s = s + current_prime
            for i in xrange(current_prime**2, n, current_prime):
                sieve[i] = False
        current_prime += 1
    return s

print sum_of_primes_2(2000000) # takes 4 seconds
