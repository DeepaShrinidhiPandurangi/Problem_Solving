# Read a file and print its alternate lines

import io
open_file = open("rosalind1.txt")
read_file = open_file.read()
print("Full file:")
print(read_file)

infile = io.StringIO(read_file) # Note , io.StringIO impersonates string data as a file.
print("Edited File:")
for i,j in enumerate(infile):
    if i%2 == 0:
        print(j.strip("\n")) # strip to remove empty lines   .strip() also works.

'''
Full file:
 Bravely bold Sir Robin rode forth from Camelot  # If you don't want the space before Bravely, type print commands separately as shown above.
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat
Edited File:
Bravely bold Sir Robin rode forth from Camelot
He was not afraid to die, O brave Sir Robin
He was not at all afraid to be killed in nasty ways
Brave, brave, brave, brave Sir Robin
'''

'''
o/p:
Full file:
Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat
Edited File:
Bravely bold Sir Robin rode forth from Camelot
He was not afraid to die, O brave Sir Robin
He was not at all afraid to be killed in nasty ways
Brave, brave, brave, brave Sir Robin
'''    