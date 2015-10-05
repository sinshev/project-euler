
def get_divisors(n):
	sieve = [1] * (n/2)
	if n%2 != 0:
		sieve[::2] = [False] * (n/4)
	for i in xrange(1, len(sieve)):
		if sieve[i] and n%i != 0:
			sieve[i] = 0
	return sum(sieve)

	# divisors_count = 0
	# for i in xrange(1,n/2):
	# 	if n%i == 0:
	# 		divisors_count += 1
	# return divisors_count

def triangle_number():	
	number = 0
	a = 0
	for i in xrange(2, 999999999999, 2):
		number = number + i
		a = get_divisors(number)
		if a >= 500:
			return number

triangle_number()
