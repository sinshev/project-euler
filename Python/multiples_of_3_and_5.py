# Problem 1
def multiples(n):
	n = n - 1
	list_of_multiples = []
	while n > 0:
		if n % 5 == 0 or n % 3 == 0:
			list_of_multiples.append(n)
		n = n - 1
	return sum(list_of_multiples)

print multiples(1000)