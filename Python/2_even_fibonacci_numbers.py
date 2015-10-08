# Problem 2
def even_fibonacci():
	a = 0
	b = 1
	c = 0
	terms_sum = 0
	while c <= 4000000:
		c = a + b
		if c%2 == 0:
			terms_sum = terms_sum + c
		a, b = b, c
	return terms_sum

print even_fibonacci()	