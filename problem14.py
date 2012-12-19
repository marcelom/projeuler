
# collatz cache
c = { 1:4, 2:2 }

def CollatzSequenceLength(n):
	# Given the number, return the length on the Collatz sequence
	# uses a cache to speed up the process...
	if n in c:
		#print "direct-cache-hit(%s)" % n,
		return c[n]
	b = [ n ]
	while True:
		d,r = divmod(b[-1],2)
		if r == 0:
			b.append(d)
		else:
			b.append(3*b[-1]+1)
		try:
			while len(b)>1:
				c[b[-2]] = c[b[-1]] + 1
				#print "cache-hit(%s)" % b[-1],
				b.pop()
			return c[n]
		except KeyError:
			# c[b[-1]] does not exist, continue...
			#print "cache-miss(%s)" % b[-1],
			pass

startnumber = 0
largestsequence = 0

for x in range(1,1000001):
	#print x,CollatzSequenceLength(x)
	z = CollatzSequenceLength(x)
	if z > largestsequence:
		largestsequence = z
		startnumber = x

print "Largest sequence is %s, starting number is %s" % (largestsequence, startnumber)

