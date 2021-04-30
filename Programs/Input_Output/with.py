'''with statement in Python
with statement in Python is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams. Observe the following code example on how the use of with statement makes code cleaner.'''

# file handling 
  
# 1) without using with statement 
file = open("/home/deepa/Desktop/test.txt","w")# "w" is write permission
file.write('hello world !') 
file.close() 
  
# 2) without using with statement 
file = open('file_path', 'w') 
try: 
    file.write('hello world') 
finally: 
    file.close() 
 

filter_none
brightness_4
# using with statement 
with open('file_path', 'w') as file: 
    file.write('hello world !') 
