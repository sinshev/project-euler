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

# print triplet() # takes 45 seconds

from itertools import permutations, product

def triplet_permutations():
	a = permutations(range(1, 500), 3)
	for i in a:
		if sum(i) == 1000 and i[0]<i[1]<i[2] and i[0]*i[0] + i[1]*i[1] == i[2]*i[2]:
			return i[0]*i[1]*i[2]

# print triplet_permutations() # takes 25 seconds

def triplet_product(): 
	a = product(range(1, 500), range(1, 500), range(1, 500))
	for i in a:
		if sum(i) == 1000 and i[0]<i[1]<i[2] and i[0]*i[0] + i[1]*i[1] == i[2]*i[2]:
			return i[0]*i[1]*i[2]

# print triplet_product() # takes 25 seconds