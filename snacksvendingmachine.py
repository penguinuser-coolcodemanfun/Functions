def calculate_Change(paid,price):
    change = paid - price
    return change


snack_price = 25

print(" ===== SNACK VENDING MACHINE ===== ")

print(f"This snack costs {snack_price} units.")
print("Accepted coins: (1,5,10,25) ")

total_inserted = 0
coins_inserted = 0

while True:

    coin = int(input(" Insert a coin (1, 5, 10, or 25)"))

    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid Code, try it again! \n")

    total_inserted += coin
    coins_inserted += 1

    print(f"Inserted {coin}. Total so far: {total_inserted} \n")

    if total_inserted >= snack_price:
            print("Enough money inserted!\n")
            break


change_Due = calculate_Change(total_inserted, snack_price)

print("Displensing your snack")

if change_Due == 0:
    pass
else:
    print(f"Here is your change: {change_Due} units")
print("\n ===== PURCHASE SUMMARY ===== ")
print("Snack Price: ", snack_price)
print("Coins Inserted", coins_inserted)
print("Total Paid: ", total_inserted)
print("Change Given: ", change_Due)
print("============================================")
print("Thanks for your purchase")