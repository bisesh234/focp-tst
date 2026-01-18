import random 

# asking user for password
password = input("enter password ")

# check password
if len(password) < 9:
    print("\n password is short")
    exit()

#ask for 3 letters
for _ in range(3):
    position = random.randint(1, len(password))
    guess = input(f"enter position {position}:")

    if guess == password[position - 1]:
       print("\nCorrect")
    else:
        print("Security check failed") 
        exit()

print("\nsecurity check passed.")          