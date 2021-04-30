'''Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

Sample Dataset
HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102   so slice the string from 22 to 28 and 97 to 103  Sample o/p : Humpty Dumpty'''


string = input("enter the string \n")
a= int(input("a is : \n"))
b= int(input("b is : \n"))
c= int(input("c is : \n"))
d= int(input("d is : \n"))
print (string[a:b+1]+' '+string[c:d+1]) # or print(string[a:b+1],string[c:d+1])
