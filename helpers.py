import operator

# On demand prime generator...
# Found this online, pretty clever function...
def Primes():
	D = {}
	q = 2
	while True:
		if q not in D:
			# not marked composite, must be prime
			yield q
			#print D
			#first multiple of q not already marked
			D[q * q] = [q] 
		else:
			for p in D[q]:
				D.setdefault(p + q, []).append(p)
			# no longer need D[q], free memory
			del D[q]
		q += 1

# Prime Decomposition, returns p1^ep1 + p2^ep2... like { p1:ep1, p2:ep2, ... }
def PrimeDecomp(n):
	d = {}
        #primes = Primes()
        for p in Primes():
		while n % p == 0:
			n /= p
			d[p] = d.setdefault(p, 0) + 1
			if n == 1:
				return d

# Returns the number of divisors of a number
def NumberOfDivisors(n):
	d = PrimeDecomp(n)
	powers_plus = map(lambda x: x+1, d.values())
	return reduce(operator.mul, powers_plus, 1)
