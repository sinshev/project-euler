# Problem 9

def triplet():
	lst = [i for i in range(1,500)]
	for i in lst:
		a = i
		for i in lst:
			b = i
			for i in lst:
				c = i
				if a<b<c and a*a+b*b==c*c and a+b+c==1000:
					return a*b*c

print triplet()