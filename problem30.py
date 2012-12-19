# max number is 354294 = 5 * (9**5)

MAX = 354294
fsum = 0

for n in range(2,MAX+3):
	nsum = 0
	for a in str(n):
		nsum += int(a)**5
	if nsum == n:
		print n
		fsum += n

print fsum

