numbers = [10, 20, 30, 90, 30, 22, 11]
total = 0

for num in numbers:
    if num > 100:
        print("Value over 100 found:", num)
        break
    total += num
    print("Running total:", total)
else:
    print("all numbers processed")
