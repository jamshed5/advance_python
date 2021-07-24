# Comparing Two Dates in Python
'''
We can compare date class and datetime class objects using == , < , >
The comparison will return either True or False

'''
from datetime import date
d_1=date(2019,6,30)
d_2=date(2010,6,30)

# complate date formate comparison
print(d_1 == d_2)
print(d_1 > d_2)
print(d_1 < d_2)
print(d_1 != d_2)

print()
# year comparison
print(d_1.year==d_2.year)

print()
# day comparison
print(d_1.day==d_2.day)

print()
# month comparison
print(d_1.month==d_2.month)
