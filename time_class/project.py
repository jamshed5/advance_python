# time class
'''
time object- a time object is an object containing information
of local time of day. independent of any particular day, and
subject to adjustment via a tzinfo object.
'''

from datetime import time 
tm= time(hour=20, minute=34, second=12)
print(tm)

print('-----')
print(tm.hour)
print(tm.minute)
print(tm.second)

print('-----')
tm2= time(22, 34, 12)
print(tm2)
print('-----')
print('--ok')
print()