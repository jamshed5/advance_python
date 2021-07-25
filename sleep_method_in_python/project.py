# Sleeping method in python 
'''
sleep() method is used to stop execution of a program temporarily
for a given amount of time. when this function is called, PVM stops 
program execution for given amount of time.
- it belongs to time module

'''
from time import sleep
for i in range(20):
    sleep(1)
    print(i)