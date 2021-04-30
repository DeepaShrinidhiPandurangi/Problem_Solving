# Remove empty lines from the file
openfile = open("L3_char.txt")
contents = openfile.read()
#print(read)

new_contents = []
for line in contents:
    # Strip whitespace, should leave nothing if empty line was just "\n"
    if not line.strip():
        continue
    # We got something, save it
    else:
        new_contents.append(line)
for i,j in enumerate(new_contents):
  if j in L:
    print("",end="")
  else:
    print(j,end="")
