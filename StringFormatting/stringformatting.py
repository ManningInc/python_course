#String Function
age = 24

print("My age is " + str(age) + " years")

#Replacement Fields
print("My age is {0} years".format(age))
#{} allows us to replace fields

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "Jan", "Mar", "May", "July", "August", "Oct", "Dec"))

print("""
Number of Days
January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

#String Formatting - Intro in Python2 but not used in Python3
# % signs should not be used in Python 3 really but will appear in python 2 code.

print("My Age is %d years" % age)
print("My Age is %d %s, %d %s" % (age, "years", 6, "months"))

print("""
With Formating""")

for i in range(1,12):
    print("No. %2d squared is %4d and the cubed is %4d" %(i, i**2, i**3))
    # ** is to the power of.
    #
    #%2d and %4d allocates spaces with blank spaces if they are not organised
    #%d is no formatting

print("""
No Formating""")

for i in range(1,12):
    print("No. %d squared is %d and the cubed is %d" %(i, i**2, i**3))

print("Pi is approximately %12.50f" %(22/7))
#f is a float so gives a decimal, eg .50f gives 50 decimal places where as f gives a default of 6.


print("""
Using Python 3 Method""")

for i in range(1,12):
    print("No. {0:2} squared is {1:4} and the cubed is {2:4}".format(i, i**2, i**3))

    #{0:2} is formatted to 2 spaces, {0:4} gives 4 spaces
    #{0:<4} means that it counts from the left rather than the right

print("""
Using Python 3 <Method""")

for i in range(1,12):
    print("No. {0:<2} squared is {1:<4} and the cubed is {2:<4}".format(i, i**2, i**3))

print ("Pi is approximately {0:12.50}".format(22/7))

for i in range(1,12):
    print("No. {:<2} squared is {:<4} and the cubed is {:<4}".format(i, i**2, i**3))

# no specified number uses it in order.
