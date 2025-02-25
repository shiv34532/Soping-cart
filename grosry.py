items_list = [
    ["Apple", [2.0, 50]],  # [price, stock]
    ["Banana", [1.0, 60]],
    ["Orange", [1.5, 40]],
    ["Milk", [3.0, 30]],
    ["Bread", [2.5, 40]]
]

daily_income = 0.0
total_customers = 0

print("Store Opening!")

opening_time = "9:00 AM"
closing_time = "9:00 PM"
print(f"Store opens at {opening_time} and closes at {closing_time}.")

try:
    num_customers = int(input("Enter the number of customers today: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    num_customers = 0

for customer_number in range(1, num_customers + 1):
    print(f"\n=== Customer {customer_number} ===")
    cart = []
    
    while True:
        print("\nAvailable items:")
        for item in items_list:
            item_name = item[0]
            item_price = item[1][0]
            item_stock = item[1][1]
            print(f"- {item_name} (Price: ${item_price}, Stock: {item_stock})")
        
        item_choice = input("Enter item name (or 'done' to finish): ").strip().capitalize()
        if item_choice == "Done":
            break
        
        found_item = None
        for item in items_list:
            if item[0] == item_choice:
                found_item = item
                break
        
        if found_item:
            try:
                quantity = int(input(f"Enter quantity of {item_choice}: "))
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue
                if quantity > found_item[1][1]:
                    print("Insufficient stock.")
                    continue
                cart.append([item_choice, quantity])
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Item not found.")
    
    print(f"\n=== Customer {customer_number} Receipt ===")
    print("Item\t\tQty\tPrice\tTotal")
    customer_total = 0
    
    for cart_item in cart:
        item_name = cart_item[0]
        quantity = cart_item[1]
        for item in items_list:
            if item[0] == item_name:
                price = item[1][0]
                total = price * quantity
                customer_total += total
                item[1][1] -= quantity
                print(f"{item_name[:7]:<7}\t{quantity}\t${price}\t${total:.2f}")
                break
    
    print("---------------------------")
    print(f"TOTAL:\t\t\t\t${customer_total:.2f}")
    daily_income += customer_total
    total_customers += 1

# End of day report
print("\n=== DAILY SUMMARY ===")
print(f"Total Customers: {total_customers}")
print(f"Daily Income: ${daily_income:.2f}")
print("\nRemaining Stock:")
for item in items_list:
    print(f"{item[0]}: {item[1][1]}")
print("====================")

print("Store Closing!")