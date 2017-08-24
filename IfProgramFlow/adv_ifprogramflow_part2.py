age = int(input("How old are you? "))
if not(age < 18):
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18-age))

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot: #in looks into the string
    #'in' is case specific
    print("Give me a {},Bob".format(letter))
else:
    print("I don't need that letter")
