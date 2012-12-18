from sets import Set

seq = []

for a in range(2,101):
	x = a
	for b in range(2,101):
		x *= a
		seq.append(x)

#sorted(seq)
#print seq
print len(set(seq))

