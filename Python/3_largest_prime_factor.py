# Problem 3
def prime_factor(n):
	i = 2
	while i * i < n:
		 while n % i == 0:
			n = n / i
		 i = i + 1
	print n

prime_factor(600851475143)