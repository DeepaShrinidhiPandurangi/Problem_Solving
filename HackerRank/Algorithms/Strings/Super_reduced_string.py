# Super reduced string

# Use slicing to delete unwanted elements


s = "baab"
i = 0
while i < len(s)-1:
  if s[i]==s[i+1]:
    s = s[:i]+s[i+2:]
    i=0
  else:
    i += 1
if s:
  print(s)
else:
  print("Empty String")
