# String manipulations 

#1. Format string by embedding variables within strings 

num = 45
str = "Ram"
decimal = 20.90
L = [1,2,3,4,5]
sentence  = "%s had %f chocolates , %d fruits and a big list of veggies %r" %(str,decimal,num,L)
print(sentence)

# o/p:
''' 
Ram had 20.900000 chocolates , 45 fruits and a big list of veggies [1, 2, 3, 4, 5]
'''

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print ("Let's talk about %s." % my_name)
print ("He's %d inches tall." % my_height)
print ("He's %d pounds heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % (my_age,my_height, my_weight, my_age + my_height + my_weight))

#o/p:
'''
Let's talk about Zed A. Shaw.He's 74 inches tall.He's 180 pounds heavy.
Actually that's not too heavy.
He's got Blue eyes and Brown hair.
His teeth are usually White depending on the coffee.
If I add 35, 74, and 180 I get 289.
'''

#2. Printing
print ("Mary had a little lamb.")
print ("Its fleece was white as %s." % 'snow')
print ("And everywhere that Mary went.")
print ("." * 10) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print (end1 + end2 + end3 + end4 + end5 + end6,)
print (end7 + end8 + end9 + end10 + end11 + end12)
print (end1 + end2 + end3 + end4 + end5 + end6,end=" ")
print (end7 + end8 + end9 + end10 + end11 + end12)

#o/p:
'''
Mary had a little lamb.Its fleece was white as snow.And everywhere that Mary went.
..........
Cheese
Burger
Cheese Burger
'''

formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))# Note the o/p
print (formatter % ("I had this thing.","That you could type up right.","But it didn't sing.","So I said goodnight."))

# o/p:
'''
1 2 3 4
one' 'two' 'three' 'four'
True False False True
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'   ## Note
'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
''' 
# Note : In the above output, "But it didn't sing." has double quotes to differentiate it from the single quote inside the string (didn't)

# 3.More printing
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"  #\n : new line character
print ("Here are the days: ", days)
print ("Here are the months: ", months)
print ("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4""")
#o/p:
'''
Here are the days:  Mon Tue Wed Thu Fri Sat SunHere are the months:  JanFeb
Mar
AprMay
Jun
Jul
Aug
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4
'''