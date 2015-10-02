# Problem 2
def even_fibonacci(n):
	a = 0
	b = 1
	c = 0
	terms_sum = 0
	for i in range(2, n + 1):
		while c <= 4000000:
			c = a + b
			if c%2 == 0:
				terms_sum = terms_sum + c
			a, b = b, c
	return terms_sum

print even_fibonacci(1000)	