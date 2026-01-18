#logical opperatoors
age = 30

print(age >= 18 and age <= 65)   # True
print(age < 18 or age > 65)      # False
print(not age > 18)              # False

#multiple logical operatrs
age = 30

print((age >= 18 and age <= 65) and (not age == 30))  # False

#chained relationship operators
weight = 150
height = 145

print(100 < weight < 200)   # True
print(131 < height < 160)   # True