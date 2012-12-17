import helpers

def TriangleNumbers():
	i = 1
	t = 0
	while True:
		t += i
		i += 1
		yield t + i

for n in TriangleNumbers():
	d = helpers.NumberOfDivisors(n)
	if d > 500:
		print n, d
		break
