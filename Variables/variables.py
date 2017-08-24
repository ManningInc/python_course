greeting = "Bruce"
_myName = "Josh"
#Starting with Numbers is not allowed

Greeting = " This is a different Variable to greeting"


age = 24

print(age)

#print (greeting + age)

a = 12
b = 3

print(a+b)
print(a-b)
print(a*b)
#Returns a Float
print(a/b)
#Returns a Integer
print(a//b)

print(a%b)

for i in range(1,a//b):
    print(i)
#multiplication and devision have higher presendiance
print(a+b/3-4*12)

print((((a+b)/3)-4)*12)

c = a + b
d = c / 3
e = d - 4
print(e*12)

#Strings

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[0])
#Negatives count from the End
print(parrot[-1])

# A Slice
print(parrot[0:6])
#missing Start number at the start
print(parrot[:6])
#Missing number prints to end
print(parrot[6:])

print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223,372,036,854,775,807"

print(number[1::4])

number = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(number[0::3])


String1 = "He's"
String2 = "probably "

print(String1 + String2)

print("Hello "*5)
print("Hello "* (5 + 4))
print("Hello " * 5 +"4")

today = "Friday"

#  'in' used to find what is contained

print("day" in today)
print("Fri" in today)
print("Thur" in today)
print("parrot" in "fjord")



