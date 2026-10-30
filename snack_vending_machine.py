def calculate_change("paid, price"):
    change=paid - price
    return change
snack_price=int(input("Enter the price of the snack: "))
print("===== Snack Vending Machine =====")
print(f"This snack costs {snack_price} units.")
print("Accepted coins: 1, 5, 10, 25\n")
total_inserted=0
coins_inserted=0
while True:
    coin=int(input("Insert a coin (1, 5, 10, 25): "))
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin. try again!\n")
    
        total_inserted += coin
        coins_inserted += 1
        print(f"Total inserted: {total_inserted} units.")
    else:
        print("Invalid coin. Please insert a valid coin.")