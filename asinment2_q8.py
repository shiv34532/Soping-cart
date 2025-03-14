qutrer = int(input("Enter the number of quarters to convert to dollars: "))
dime = int(input("Enter the number of dimes to convert to dollars: "))
nucal = int(input("Enter the number of nickels to convert to dollars: "))
peni = int(input("Enter the number of pennies to convert to dollars: "))

qutra_value = qutrer * 0.25
dime_value = dime * 0.10
nucal_value = nucal * 0.05
peni_value = peni * 0.01

total_value = qutra_value + dime_value + nucal_value + peni_value

print(f"Value of quarters: ${qutra_value:.2f}")
print(f"Value of dimes: ${dime_value:.2f}")
print(f"Value of nickels: ${nucal_value:.2f}")
print(f"Value of pennies: ${peni_value:.2f}")
print(f"Total value of change: ${total_value:.2f}")
