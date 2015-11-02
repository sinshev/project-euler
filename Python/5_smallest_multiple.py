# Problem 5

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
	        n /= i
	        factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def smallest_multiple(n):
	factors = [prime_factors(i) for i in xrange(1,n+1)]
	primes = {}
	for item in factors:
			for i in item:
				count = item.count(i)
				if i in primes:
					if primes[i] < count:
						primes[i] = count
				else:
					primes[i] = 1
	smallest_multiple = 1
	for k,v in primes.iteritems():
		smallest_multiple *= k**v
	return smallest_multiple

print smallest_multiple(20)
