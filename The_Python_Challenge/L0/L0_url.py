#Prob.1
'''
http://www.pythonchallenge.com/pc/def/0.html
Hint: try to change the URL address. URL:Uniform resourse locater(Web address)
Most web browsers display the URL of a web page above the page in an address bar. 
A typical URL could have the form http://www.example.com/index.html, which indicates a protocol (http), a hostname (www.example.com), and a file name (index.html).
The picture shows 2^38.
'''

#Code
n = int(input("enter the base \n"))
x = int(input("enter the exponent \n"))
res = (n)**(x)
print(res)
 
'''O/p:
enter the base
2
enter the exponent
38

274877906944

'''
# Enter this result in the place of "0" in the URL index. Remove commas (if any)from the number as http addresses should generally not have commas as a good practice