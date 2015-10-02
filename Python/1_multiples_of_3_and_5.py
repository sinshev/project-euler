# Problem 1
def multiples(n):
	n = n - 1
	multiples_sum = 0
	while n > 0:
		if n % 5 == 0 or n % 3 == 0:
			multiples_sum = multiples_sum + n
		n = n - 1
	return multiples_sum

print multiples(1000)