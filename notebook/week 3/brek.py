numbers = [10, 20, 30, 90, 200, 30, 22, 11]
total = 0
for num in numbers:
    if num > 100:
        print("value of 100 found", num)
        break
    total +=num
    print("running total", total)
    