foods = []
prices=[]
total = 0;
while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower()=="q" :
        break
    else:
        price = float(input("Enter price of the food : "))
        foods.append(food)
        prices.append(price)
        total+=price
print("---------------YOUR CART---------")
for i in range(len(foods)) :
    print(foods[i], end="  ")
    print(prices[i],end="  ")

    print()
print(f"Total: {total}")