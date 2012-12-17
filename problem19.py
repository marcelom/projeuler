# 1 Jan 1900 was a Monday.
# Thirty days has September, April, June and November. All the rest have thirty-one, Saving February alone,
# Which has twenty-eight, rain or shine. And on leap years, twenty-nine. A leap year occurs on any year
# evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

day = 7
month = 1
year = 1900

sundays = 0

while year < 2001:
	day += 7
	if month in [ 4, 6, 9, 11 ]:
		mdays = 30
	elif month == 2:
		mdays = 28
		if year % 4 == 0:
			mdays = 29
			if year % 100 == 0 and year % 400 !=0:
				mdays = 28
	else:
		mdays = 31

	if day > mdays:
		month +=1
		day -= mdays
	if month > 12:
		month -= 12
		year += 1
	if day == 1 and year > 1900 and year < 2001:
		sundays += 1
	#print day, month, year, sundays

print sundays

