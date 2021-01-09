"""Create a calandar for the current month, in markdown"""

from datetime import datetime, timedelta

week_header = "| M  | T  | W  | T  | F  | S  | S  |\n"
header_line = "| -  | -  | -  | -  | -  | -  | -  |\n"

def get_last_day_of_month(today):
	# Guaranteed to get the next month. Force any_date to 28th and then add 4 days.
	next_month = today.replace(day=28) + timedelta(days=4)
	 
	# Subtract all days that are over since the start of the month.
	return (next_month - timedelta(days=next_month.day)).day
 


# today = datetime.today()
today = datetime(2020, 2, 1)


first_day_of_month = datetime(today.year, today.month, 1)
weekday_start = first_day_of_month.weekday()

first_week = ""
empty_day = "|    "

day_of_month = 1
last_day_of_month = get_last_day_of_month(today)


for i in range(weekday_start):
	first_week += empty_day

for i in range (weekday_start, 7):
	first_week += "| " + str(day_of_month) + "  "
	day_of_month += 1


first_week += "|\n"

full_weeks = ""

for i in range(4):
	for i in range(7):

		if day_of_month > last_day_of_month:
			full_weeks += "|    "
		else:
			if day_of_month < 10:
				full_weeks  += "| " + str(day_of_month) + "  "
			else: 
				full_weeks  += "| " + str(day_of_month) + " "

		day_of_month += 1
	full_weeks += "|\n"


cal = week_header + header_line + first_week + full_weeks

print cal