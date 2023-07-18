# import datetime moduals
from datetime import date, datetime

# get a string of todays date
today = date.today()
today = str(today)

# write that string to a txt file
txt = open("today.txt", "w")
txt.write(today)
txt.close()

# read that textfile
txt = open("today.txt", "r")
today_string = txt.read()
txt.close()
print(today_string)

# Parse data in textfile and output it
parseToday = datetime.strptime(today_string, '%Y-%m-%d')
print(f"""Today's Date:
Year  = {parseToday.year}
Month = {parseToday.month}
Day   = {parseToday.day}""")