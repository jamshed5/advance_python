# datatime module 
'''
datetime - it handles date and time. its has year,month, day, hour, minutes, seconds microsecond and tzinfo attributes

date- it handles dates of gregorgian calender, without talking time zone into 
consideration. it has year, month and day attributes.

time- it handles time assuming that every day has exactly 24x60 seconds. it has hours, minutes, seconds, microsecond
and tzinfo attributes

timedelta- it handles durations. The duration may be the difference between two date,
time or datetime instance.

datetime object- a datetime object is a single object containing all the information from a date object and a time object
'''

'''
datetime class methods
now() this method is used to get the current date and time. we
can provide timezone information to this method. if the timezone
is not provided, then it takes the local time zone. it returens an
object that contains date and time information in any timezone.
we can use dat, month, hour, minutes and second.
'''
from datetime import datetime

dt1=datetime(year=2017, month=1, day=4)
dt2=datetime(year=2018, month=12, day=5, hour=18, minute=20)
dt3=datetime(2013,4,3)
dt4=datetime(2018,3,27,14,30)


print(dt1)
print(dt2)
print(dt3)
print(dt4)
print(dt4.year)
print(dt4.month)
print(dt4.day)

print(datetime.now())
print(datetime.today())

print('-----')
dt5=datetime.today()
print(dt5.year)
print(dt5.day)
print(dt5.month)