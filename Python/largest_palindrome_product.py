# Problem 4
def if_palindrome(n):
	a = str(n)
	if len(a)==6:
		if a[:3] == a[::-1][:3]:
			return True
	elif len(a)==5:
		if a[:2] == a[::-1][:2]:
			return True

def largest_palindrome():
	x = 999
	y = 999
	products = []
	while x>=100:
		for i in xrange(100,y+1):
			z=x*i
			if if_palindrome(z):
				products.append(z)
		x=x-1		
	return max(products)

print largest_palindrome()