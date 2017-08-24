age = int(input("How old are you? "))

#if (age >=16) and (age <= 65): #looks for the Range between 16 and 65
# if 15 < age < 66:
#     print("Have a good day at work")
    #Brackets (Parentatesis) make things easier to read and also make you intentions in the code clearer.

if (age < 16) or (age > 65): #Or looks for the positive whereas And looks for the negative
    print("Enjoy your free time")
else:
    print("have a good day at work")

#if (some_condition) or (some weird function that does stuff()):
    #do something

#Booleans don't exist in Python

x = "false"

if x:
    print("x is true")

x = input("Please Enter some Text ")

if x:
    print("You entered '{}'".format(x))
else:
    print("Plese enter something")

print(not False)
print(not True)

