#One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

import string
openfile = open("L4_char.txt")
contents = openfile.read()
#print(read)
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
new_contents = ""
check = ""
res_counter=0
res_mid_letter = ""
for line in contents:
    # Strip whitespace, should leave nothing if empty line was just "\n"
    if not line.strip():
        continue
    # We got something, save it
    else:
        new_contents= new_contents+line
#print(new_contents)

for i in range(0,len(new_contents)):
    check = new_contents[i:i+9]
    #print(check)
    flag =0 # Flag is for every word len(10)).Evert time a new 10 letter word is read, the flag has to be reset.
    if len(check) == 9:
        first = check[0]
        second = check[1:4]
        third = check[4]
        fourth = check[5:8]
        fifth = check[8]
        count = 0 
        for j in range(0,len(second)):
            if second[j] in uppercase:
                count = count+1
                if count == 3:
                    flag = flag+1
        if first in lowercase:
            flag = flag+1
        if third in lowercase:
            flag = flag+1
        if fifth in lowercase:
            flag = flag+1
        count = 0
        for k in range(0,len(fourth)):
            if fourth[k] in uppercase:
                count = count+1
                if count == 3:
                    flag = flag+1
        #print(flag)
        if flag == 5:
            print(first,second,third,fourth,fifth)
            res_counter = res_counter+1
            res_mid_letter = res_mid_letter + third
            print(res_counter)
#print(res_mid_letter)

'''
q IQN l QSL i
1
e OEK i VEY j
2
a ZAD n MCZ q
3
b ZUT k LYN g
4
u CND e HSB j
5
k OIX d KBF h
6
d XJV l GZV m
7
g ZAG i LQZ x
8
v CJA s ACF l
9
q KWG t IDC j
10
linkedlist
'''
# Enter linkedlist.php in place of equality.html
        