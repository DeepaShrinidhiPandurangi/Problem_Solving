'''Day 6: Strings : To read and manipulate multiple lines of Strings

Objective 
Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops. 
Check out the Tutorial tab for learning materials and an instructional video!
Task 
Given a string,S , of length N that is indexed from 1 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).
Note: 0 is considered to be an even index.

Input Format
The first line contains an integer, T (the number of test cases). 
Each line i of the T subsequent lines contain a String,S .

Constraints
1<= T<= 10
2<= length of S <= 10000
Output Format
For each String Sj (where0<= j <= T-1 ), print Sj's even-indexed characters, followed by a space, followed by Sj's odd-indexed characters.

Sample Input
2
Hacker
Rank

Sample Output
Hce akr
Rn ak  '''
T=int(input("")) # Number of lines of String , if 2, the input can take 2 strings from the user, one at a time to be typed in stdin.
for i in range(0,T):  # starts from 0th line of the input. 1st line is numbered from 0.
    S=str(input(""))
    string1="" ### Note: Make sure the initialization is done here and not outside the for loop.
    string2=""
    for k,l in enumerate(S):
        if k%2==0:
            string1= string1+S[k]
        else:
            string2= string2+S[k]
    print(string1+" "+string2)
    
'''# Single line code on HackerRank:
for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])   '''
    
'''Output:
Compiler Message
Success

1.
Input (stdin)Download
2
Hacker
Rank
Expected OutputDownload
Hce akr
Rn ak

2.
Input (stdin)Download
10
ovyvzvptyvpvpxyztlrztsrztztqvrxtxuxq
holtm
uvzxrumuztyqyvpnji
tmruzxzuwoskqysxztuvosuyrswrnmtxvzsrqwytzrxpltrwusxupw
wxstwxuzuyuvyzrsxysxyuvyqxuxyskqwsyqumqrvopvowqumnvrxpwqpwsrnvrztxrxpvuxunvyzvupvupowvyzvzuzwvsrwv
yrzxrxskrtlpwpmtpxvowrxrpxq
pryumtuntmovpwvowslj
nosklrxrtyuxtmnurzsryuxtywqwqpxts
fmpszyvqwxrtvpuwqszvyvotmsxsxuvzyvpwzrpmuxqwtswvytytzsnuxuyrpvtysqoutzurqxury
jkmsxzwrxzy

Expected OutputDownload
oyzpyppytrtrttvxxx vvvtvvxzlzszzqrtuq
hlm ot
uzrmzyypj vxuutqvni
trzzwsqszuourwntvsqyzxlruxp muxuokyxtvsysrmxzrwtrptwsuw
wswuuuyrxsyvquykwyuqvpoqmvxwpsnrtrpuuvzuvpwyvuwsw xtxzyvzsyxuyxxsqsqmrovwunrpqwrvzxxvxnyvpuovzzzvrv
yzrsrlwmpvwxpq rxxktpptxorrx
pymutopvwl rutnmvwosj
nslxtutnrsyxyqqxs okrryxmuzrutwwpt
fpzvwrvuqzyomxxvypzpuqtwyyznxyptsotuquy msyqxtpwsvvtssuzvwrmxwsvttsuurvyquzrxr
jmxwxy kszrz '''