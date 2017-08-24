name = input("Please Enter Your Name Here ")
age = int(input("How old are you?, {0}? "Jo.format(name)))

if (age < 18) or (age > 30):
    print("Sorry you age does not qualify for this holiday package")
else:
    print("Welcome to the holiday, {0}".format(name))

