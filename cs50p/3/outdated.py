"""
Program that prompts the user for a date in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format,
prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input('Date: ').strip()
        date = date.split(' ')
        if len(date) == 1:
            date = date[0].split('/')
            day = int(date[1])
            month = int(date[0])
        elif ',' in date[1]:
            day = int(date[1].removesuffix(','))
            month = months.index(date[0]) + 1
        year = int(date[2])
        if 1 <= day <= 31 and 1 <= month <=12: break
    except (TypeError, ValueError, NameError):
            pass

print(f'{year}-{month:02}-{day:02}')
