# Problem 4
def if_palindrome(n):
	a = str(n)
	return (a == a[::-1])

def largest_palindrome():
	x = 999
	y = 999
	max_product = 0
	while x>=100:
		for i in xrange(100,y+1):
			z=x*i
			if if_palindrome(z) and z > max_product:
				max_product = z
		x=x-1		
	return max_product

print largest_palindrome()