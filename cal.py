"""Create a calandar for the current month, in markdown"""

from datetime import datetime, timedelta

week_header = "| M  | T  | W  | T  | F  | S  | S  |\n"
header_line = "| -  | -  | -  | -  | -  | -  | -  |\n"
empty_day = "|    "


def get_last_date_of_month(today):
	# Guaranteed to get the next month. Force any_date to 28th and then add 4 days.
	next_month = today.replace(day=28) + timedelta(days=4)
	 
	# Subtract all days that are over since the start of the month.
	return (next_month - timedelta(days=next_month.day)).day


def create_first_partial_week(day_of_month):
	week = ""

	for i in range(7):
		if i >= first_day_of_month:
			week += "| " + str(day_of_month) + "  "
			day_of_month += 1
		else:
			week += empty_day

	week += "|\n"
	return week, day_of_month


def get_remaining_weeks(day_of_month):

	remaining = ""

	for i in range(4):
		for i in range(7):

			if day_of_month > last_date_of_month:
				# fill remaining days with blank spaces
				remaining += empty_day
			else:
				remaining  += "| " + str(day_of_month) + " "
				if day_of_month < 10:
					# padding for single digit dates
					remaining  += " "

			day_of_month += 1
		remaining += "|\n"
		if day_of_month > last_date_of_month:
			# if last day of the month ends on a Sunday, we don't need to 
			# write a blank week
			break

	return remaining

# today = datetime.today()
today = datetime(2020, 2, 1)

# Get first day of the month (0 as Mon, 1 as Tues etc)
first_day_of_month = datetime(today.year, today.month, 1).weekday()

# Get last date of the month, 30, 31 etc
last_date_of_month = get_last_date_of_month(today)


day_of_month = 1

first_week, day_of_month = create_first_partial_week(day_of_month)
remaining_weeks = get_remaining_weeks(day_of_month)

cal = week_header + header_line + first_week + remaining_weeks

print cal
