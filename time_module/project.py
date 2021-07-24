'''
following modules are used to work with date, time and duration 
- time 
- datetime 
'''
'''
time() function - this function return the time in second since the epoch as a 
floating point number. the specific data of the epoch and the handling of leap
seconds of platform dependent 

ctime() function this function is used to get current date and time. when we pass
epcoh time in seconds to the function, it returns corrsponding date and time in  striing 
formate

localtime() function - this function is used to covert second into date and time .
it returns an object struct_time whcih can be used to access the attributes either 
using an index or using name

'''
from time import time, ctime, localtime

tm=time()
print(tm)

ct=ctime(tm)
print(ct)

print ('---or---')
print(ctime())

print('--------------')
lct=localtime()
print(lct)
print(lct.tm_year)
print(lct.tm_yday)
