
def get_divisors(n):
	divisors_count = 0
	for i in xrange(1,n/2):
		if n%i == 0:
			divisors_count += 1
	return divisors_count

def triangle_number():	
	number = 0
	a = 0
	while a <= 500:
		for i in xrange(2, 999999999999, 2):
			number = number + i
			# print number
			a = get_divisors(number) 
	return number

triangle_number()