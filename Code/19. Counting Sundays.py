'''
	You are given the following information, but you may prefer to do some research for yourself.
	- 1 Jan 1900 was a Monday.
	- Thirty days has September,
	April, June and November.
	All the rest have thirty-one,
	Saving February alone,
	Which has twenty-eight, rain or shine.
	And on leap years, twenty-nine.
	- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
	How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def problem_19(start_year, stop_year, start_dow, dow):
    counts = 0
    for year in range(start_year, stop_year + 1):
        for month in range(1, 13):
            if month in [9, 4, 6, 11]:
                days = 30
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                days = 31
            elif month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
                days = 29
            else:
                days = 28
            start_dow = (days + start_dow) % 7
            if start_dow == 6:
                counts += 1
    return counts

print(problem_19(1901, 2000, 1, 6))