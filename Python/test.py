
def get_divisors(n):
	divisors_count = 0
	for i in xrange(1,n+1):
		if n%i == 0:
			divisors_count += 1
	return divisors_count

def triangle_number():	
	number = 0
	a = 0
	for i in xrange(2, 99999999, 2):
		number = number + i
		a = get_divisors(number)
		if a >= 500:
			return number

# triangle_number()
# print get_divisors(9999999)