import helpers

amicable = []
psum = 0

for p in range(1,10001):
	if p in amicable:
		break
	a1 = sum(helpers.Divisors(p))
	a2 = sum(helpers.Divisors(a1))
	print p, a1, a2
	if a2 == p:
		print a2
		psum += p
		amicable.append(p)
		amicable.append(a1)

print ps
