age = 35

if age > 100:
    print("you are very old")
elif age > 80:
    print("you are fairly old")
elif age > 40:
    print("you are middle aged")
elif age >= 30:
    print("you are in your thirties")
else:
    print("you are not very old yet")

#explict condition
name = input("Enter your name: ")

if name != "":
    print("Your name is", name)
else:
    print("Name not entered")
    