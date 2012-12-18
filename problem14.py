
c = {}

# fill the lookup table first...

for i in range(1, 100, 2):
	a1 = (i-1)/3
	even = (i+1)/2
	c[i] = odd
	c[i+1] = even

print c

sdfsd


def collatz(n):
	s = []
	x =n
	while True:
		x = c[x]
		s.append(x)
		if x == 1:
			break
	return s

print max( [ collatz(i) for i in range(1, 1000001) ] )
