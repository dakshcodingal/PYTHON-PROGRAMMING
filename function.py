def greet_customer
    print("Welcome to the lemonade stand!")
    print("Fresh lemonade, just for you. ")


    greet_customer()


    price_per_cup=float(input("Enter the price per cup in dollars:"))
    cups_sold=int(input("Enter the number of cups sold: "))


    def calculate_total(price, cups):
        total = price * cups
        return total


        total_cost=calculate_total(price_per_cup, cups_sold)


        rounded_total=round(total_cost, 2)
        print("Total cost:", rounded_total)


        amount_paid=float(input("Enter the amount paid by the customer in dollars:"))


        def calculate_change(paid, total):
            change=paid-total
            return change


            change_due=calculate_change(amount_paid, rounded_total)