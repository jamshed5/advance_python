# opening file in python
'''
if we want to use a file or its data, first we have to open it.
open() function is used to open a file. it returns a pointer to the beginning of the file.
This is called file handles or file object.
Syntax: 
open('filename', mode='r', buffering, encoding=none, errors=None, newline=None, closefd=True, opener=None)

'''
f=open('info.txt','r')
print(f)