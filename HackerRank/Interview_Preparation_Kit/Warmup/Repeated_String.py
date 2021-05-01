# In this problem, you can count the number of "a's" without having to generate the entire string using the concepts of integer division (which gives the quotient) and modulus (which gives the remainder)


s = "kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm"
n = 736778906400
quotient = n//len(s)
rem = n % len(s)
#print(quotient)
#print(rem)
if n == 0:
  res = 0
if n < len(s):
  res = s[0:n+1].count("a")
else:
  extra = s[0:rem].count("a")
  res = s.count("a")*quotient + extra
print(res)


# or 
s="aba"
n=10
count_a_quotient = 0
count = s.count("a")
if s == "a":
  res = n
else: 
  count_a_quotient = count*((n//len(s))) # (n//len(s)) = number of times a has to be multiplied (equals number of times the string will be multiplied)
  rem_len = n-(len(s)* (n//len(s)))
  res = s[0:rem_len].count("a")
  res = res + count_a_quotient
print(res)

'''
# Test Cases 

s="kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm"
n= 736778906400


s="udjlitpopjhipmwgvggazhuzvcmzhulowmveqyktlakdufzcefrxufssqdslyfuiahtzjjdeaxqeiarcjpponoclynbtraaawrps"
n=872514961806
'''
