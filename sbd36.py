#convert into string to datetime

from datetime import datetime

date = "oct 14 1997 7:15AM"
print (type(date))

date_time = datetime.strptime(date, "%b %d %Y %I:%M%p")
print (date_time)
print (type(date_time))