import operator
import itertools

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

def Divisors(n):
	if n == 1:
		return [1]
	d = PrimeDecomp(n)
	l = list(itertools.chain(*([k] * v for k, v in d.iteritems())))
	#print l
	factors = set(itertools.chain(*(itertools.permutations(l, i) for i in range(1,len(l)+1))))
	#print factors
	divs = set(reduce(operator.mul, fs, 1) for fs in factors)
	#print divs
	return sorted([1]+list(divs))
