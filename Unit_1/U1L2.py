"""U1L2 - Data Types and Variables"""

##########################
#        Integers        #
##########################
print(3) #Like in math an integer is a whole number
print(3*3) #What will this print out?
print(10//5) #Remember we need the double // to get back just a whole number

##########################
# Floating Point Numbers #
##########################
print(3.2) #Floating points are a fancy way of saying a number with a decimal
print(10/5) #Notice the difference in the answer here than above

##########################
#         Strings        #
##########################
print("Strings") #A string is anything inside of quotes
print("3") #That means a number inside quotes is not a number, but a string
print("3"*3) #Notice what happens here, is different than what happened above

##########################
#         Boolean        #
##########################
print(True) #This data type is either True or False
print(False) #It looks like it prints as a string, but it is different
print(True * 2) #Notice how this prints, showing it's not a string
#print(False * 2) #What do you think this will print? Uncomment to find out
"""There are more data types and we will learn
   some more soon, but we'll start with these"""

##########################
#       Variables        #
##########################
x = 3 #here the variable x is assigned the value 3
print("f(x) =", 2*x+6) #What do you think this should print out then?
y = "3" #here y is assigned the character of 3
print("f(y) =", 2*y+6) #notice how this line errors out our program
#^^ Comment this line out once you've seen it fail ^^
variable = "This is a string"
#print(variable) #What do you think this will print? Uncomment to find out
age = 31 #here our variable name helps us understand what the number is
print("Your age in Months is:", age * 12)
degCel = 12 #we call this naming structure cammelCase
degFah = degCel * (9/5) + 32 #we can use variables inside of variables
cookieClicks = 0
cookieClicks = cookieClicks + 1 #what do you think the value of cookieClicks is now?
print("Print cookieClicks here to find out:",)
cookieClicks += 1 #What about this line?
print("Print cookieClicks here to find out:",)
cookieClicks -= 1 #do you think we can do this?
cookieClicks *= 2 #how about this?
#vv Add print statments below to see how cookieClicks changes vv
