from sets import Set

#seq = Set([])
seq = []

for a in range(2,101):
	for b in range(2,101):
		seq.append(a**b)

#sorted(seq)
#print seq
print len(set(seq))

