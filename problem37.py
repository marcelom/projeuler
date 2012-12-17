import helpers

primes = []
truncatable = []

for i in helpers.Primes():
	primes.append(i)
	if i<10:
		continue
	d = 1
	ltor = i
	while ltor > 1:
		d *= 10
		ltor, rtol = divmod(i, d)
		print i,ltor,rtol
		if ltor <2:
			break
		if ltor in primes and rtol in primes:
			continue
	else:
		truncatable.append(i)
	if len(truncatable) > 2:
		break

print primes, truncatable

