print("----- Beckket Pizza Plaza 4-for-3 offer------")
print("==============================================\n")

prices = []
pizza_number = 1

#input prices 

while len(prices) < 4 :
    try :
        price = float(input(f"Enter Price of Pizza {pizza_number}:"))
        if price <= 0:
            print("Please enter valid prices")
        else:
            prices.append(price)
            pizza_number += 1
    except ValueError:
        print("please enter a valid price!")

total_price = sum(prices)
free_pizza = min(prices)
final_total = total_price - free_pizza
discount_percentage = (free_pizza / total_price) * 100

print(f"\nOrder Total is £{final_total:.2f}, "
      f"a fabulous discount of {discount_percentage:.0f}%!")