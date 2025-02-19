cart = {}  # Initialize an empty dictionary to store items and prices

while True:
    item = input("Enter item name (or type 'done' to finish): ")
    if item.lower() == 'done':
        break

    while True:  # Inner loop for price input with validation
        try:
            price = float(input("Enter price for " + item + ": "))
            if price <= 0:
                print("Price must be greater than zero. Please try again.")
            else:
                break  # Exit inner loop if price is valid
        except ValueError:
            print("Invalid input. Please enter a number for the price.")

    cart[item] = price  # Add item and price to the cart dictionary

print("\n--- Shopping Cart ---")
if not cart:  # Check if the cart is empty
    print("Your cart is empty.")
else:
    total = 0
    for item, price in cart.items():  # Iterate through the cart items
        print(f"{item}: ${price:.2f}")  # formatted to two decimal places
        total += price
    print(f"--------------------")
    print(f"Total: ${total:.2f}")