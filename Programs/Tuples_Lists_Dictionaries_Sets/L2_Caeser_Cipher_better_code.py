# Assign alphabet value to all the lower and upper alphabets
def caeser_cipher(s,shift):
    import string
    result=""
    alpha_l = string.ascii_lowercase
    alpha_u = string.ascii_uppercase
    # shifted alphabets
    alpha_l_shift = alpha_l[shift:]+alpha_l[:shift]
    alpha_u_shift = alpha_u[shift:]+alpha_u[:shift]
    alphabet_l= dict()
    alphabet_u = dict()
    for i,j in enumerate(alpha_l):
        alphabet_l[j] = alpha_l_shift[i]
    #print(alphabet_l)
    for i,j in enumerate(alpha_u):
        alphabet_u[j]= alpha_u_shift[i]
    #print(alphabet_u)
    for i in range(0,len(s)):
        if s[i] in alpha_l:
            result= result+alphabet_l[s[i]]
        elif s[i] in alpha_u:
            result= result+alphabet_u[s[i]]
        else:
            result=result+s[i]
    return result

    # print(alphabet_l["a"])
    # print(alphabet_l["z"])
    # print(alphabet_l["d"])
    # print(alphabet_u["B"])
    # print(alphabet_u["Z"])
    # print(alphabet_u["S"])
    # print(alphabet_u["P"])


print(caeser_cipher(" g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.",2))
# To go to the next challenge, replace the URL "map" with "ocr".

# Or combined code (single dictionary)
import string
s= input("enter the string\n")
shift = 2
l = string.ascii_lowercase
u = string.ascii_uppercase
alpha = l+u
dict_alpha = {} #or dict()
l_shifted = l[shift:]+l[:shift]
u_shifted = u[shift:]+u[:shift]
alpha_shifted = l_shifted+u_shifted
for i,j in enumerate(alpha):
  dict_alpha[j] = alpha_shifted[i]
print(dict_alpha)

for i,j in enumerate(s):
  if j in dict_alpha:
    print(dict_alpha[j],end="")
  else:
    print(j,end="")
'''
o/p:
enter the string
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
{'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i', 'h': 'j', 'i': 'k', 'j': 'l', 'k': 'm', 'l': 'n', 
'm':'o', 'n': 'p', 'o': 'q', 'p': 'r', 'q': 's', 'r': 't', 's': 'u', 't': 'v', 
'u': 'w', 'v': 'x', 'w': 'y', 'x': 'z', 'y': 'a', 'z': 'b', 'A': 'C', 'B': 'D', 
'C': 'E', 'D': 'F', 'E': 'G', 'F': 'H', 'G': 'I', 'H': 'J', 'I': 'K', 'J': 'L', 'K': 'M', 'L': 'N', 'M': 'O', 
'N': 'P', 'O': 'Q', 'P': 'R', 'Q': 'S', 'R': 'T','S': 'U', 'T': 'V', 'U': 'W', 'V': 'X', 'W': 'Y', 'X': 'Z', 'Y': 'A', 'Z': 'B'}
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long.
 using string.maketrans() is recommended. now apply on the url.
 '''
 #Applying this on the index of the URL makes http://www.pythonchallenge.com/pc/def/map.html map > ocr. Make map to ocr.