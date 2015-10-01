# Problem 2
def even_fibonacci(n):
	terms = []
	even_terms = []
	a = 0
	b = 1
	for i in range(2, n + 1):
		c = a + b
		a, b = b, c
		if c <=4000000:
			terms.append(c)
	for x in terms:
		if x%2 == 0:
			even_terms.append(x)
	return sum(even_terms)

print even_fibonacci(1000)	