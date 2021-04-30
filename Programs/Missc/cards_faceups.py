import random
a= int(input("How many cards do you want in your deck?\n"))
fd= int(input("How many face down cards do you want to have?\n"))
fu= a-fd
face_up=""
face_down=""
index1=0
index2=0
bit=0
inverted_bit=0
print ("The number of face up cards in the deck now are (denoted by 1's):\n",fu)
print ("The number of face down cards you chose in the deck now are (denoted by 0's):\n",fd)

#make bit string out of the input
while index1 < fu:
 face_up=face_up+"0"
 index1= index1+1
while index2 < fd:
 face_down=face_down+"1"
 index2= index2+1
string= face_up+face_down
print("The deck of cards contain the following cards:\n",string)

#shuffle
b=input("Do you want to shuffle the cards to see the magic? Type 'Y' for yes or 'N' for no \n")
if b== "Y"or b=="y":
    l = list(string)
    random.shuffle(l)
    result = ''.join(l)
    print("The shuffled cards are:",result)
    print("Now the card deck is divided into 2 parts.")
    Part1=0
    Part2=0
    Part1 = result[0:fd]
    Part2= result[fd:len(result)]


    #bit reversal:
    fin_str=""
    str_len = len(Part1)
    while bit < str_len:
     letter= Part1[bit]
     if letter  == "1":
      fin_str=fin_str+"0"
      bit = bit +1
     else:
      fin_str=fin_str+"1"
      bit = bit +1
    print("Part1 of the deck is",fin_str)
    print("Part2 of the deck is",Part2)

    print("The Number of face_up card in Part 1 is :\n",fin_str.count("1"))
    print("The Number of face_up card in Part 2 is :\n",Part2.count("1"))

    LHS=0
    RHS=0
    LHS=fin_str.count("1")
    RHS=Part2.count("1")
    if LHS == RHS:
     print("Sucess,Yayyyyyy!!!!!!")
else:
    print("Thanks for playing so far.Hope to catch you soon\n")
