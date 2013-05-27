# Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
# Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

EXT1 = { 1:'one', 2:'two', 3:'three', 4 :'four', 5:'five', 6:'six', 7: 'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve',
	    13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen' }
EXT2 = { 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}



def extenso(n):
	if n == 1000:
		return "one thousand"
	if n == 100:
		return "one hundred"
	elif n == 0:
		return 'zero'
	elif n in EXT1:
		return EXT1[n]
	elif n in EXT2:
		return EXT2[n]
	if n > 100:
		n = str(n)
		if n[1:] == '00':
			return '%s hundred' % EXT1[int(n[0])]
		else:
			return '%s hundred and %s' % (extenso(int(n[0])), extenso(int(n[1:])))
	if n >= 20:
		# n here must be more than 20, or there is a bug...
		n = str(n)
		if n[1] == '0':
			return EXT2[int(n[0])]
		else:
			return '%s %s' % (EXT2[int(n[0])], EXT1[int(n[1])])

charcount = 0

for a in range(1, 1001):
	# print a, extenso(a)
	charcount += len(extenso(a).replace(' ', ''))

print charcount
