# Read the file
Open = open("test.txt")# or file path
Read = Open.read()
import io
infile = io.StringIO(Read)

for line,i in enumerate(infile):
    if line%2 == 0:
        print(i.strip())
        
   
