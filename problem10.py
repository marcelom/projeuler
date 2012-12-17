import helpers

psum = 0

for p in helpers.Primes():
	if p > 1999999:
		break
	psum += p

print psum
