# # Problem 5
# def multiplies(n):
# 	a = [i for i in xrange(11,21) if n%i==0]
# 	return a

# def smallest_multiple():
# 	# primes product - 90 (number will ends with 00)
# 	primes = 2*3*5*7*11*13*17*19-90
# 	for i in xrange(primes,primes**2, 40):
# 		if len(multiplies(i))==10:
# 			print i
# 			return
# smallest_multiple()

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
	# print factors
	primes = {}
	for item in factors:
			for i in item:
				count = item.count(i)
				if i in primes:
					if primes[i] < count:
						primes[i] = count
				else:
					primes[i] = 1
	# print primes
	# print primes.keys()
	# print primes.values()
	smallest_multiple = 1
	for k,v in primes.iteritems():
		smallest_multiple *= k**v
	print smallest_multiple



smallest_multiple(10)
