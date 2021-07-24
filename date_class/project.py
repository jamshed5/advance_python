# date class
'''
data object - a date object is an object contaning information of 
year, month and day 

all argument are required. arguments amy be integers, in the 
following ranges:
year
month
day

today() method -this method is used to get the current date. it returns only date

'''

from datetime import date
dt1= date(year=2019, month=5, day=3)
print(dt1)


dt2= date(2017, 5, 3)
print(dt2)

dt3= date.today()
print(dt3)
print(dt3.year)
print(dt3.day)
print(dt3.month)