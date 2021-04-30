# 4. BA1C Reverse complement of a string 

s = "AAAACCCGGT"
s = s[::-1]
rev_comp = ""
for i,j in enumerate(s):
  if j == "C":
    rev_comp = rev_comp + "G"
  elif j == "G":
    rev_comp = rev_comp + "C"
  elif j == "A":
    rev_comp = rev_comp + "T"
  elif j == "T":
    rev_comp = rev_comp + "A"
print(rev_comp)

# o/p : ACCGGGTTTT