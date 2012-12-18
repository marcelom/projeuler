
c = {}

# fill the lookup table first...

for i in range(1, 20, 2):
	odd = 3*i+1
	even = (i+1)/2
	c[i] = c.get(odd, -odd) +1
	c[i+1] = c.get(even, -even) +1

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
