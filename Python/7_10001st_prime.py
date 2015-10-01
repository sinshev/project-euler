# Problem 7
def find_prime(n):
	primes = [i for i in xrange(2, n)]
	a = 0
	p = 2
	while p*p < n:
		for i in xrange(2*p,n,p):
			if i in primes:
				primes.remove(i)
		p=primes[a+1]
		a = a+1
	print primes

# find_prime(104744)

def rwh_primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

# print rwh_primes(105000)[10000]

def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count<=2:
        return n
j=1
p=[2]
count=1
while len(p)<10002:
    j=j+2
    if prime(j)!=None:
        count=count+1
        p=p+[prime(j)]
        if count==10001:
            print j