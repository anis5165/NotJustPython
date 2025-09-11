print("\n\n*******************Rent Calculator************************")
rent = int(input("Enter total rent amount: "))
persons = int(input("Enter number of roommates: "))
food = int(input("Total food ordered for snacking: "))
electricity_spend = int(input("Total electricity spend: "))
charge_per_unit = int(input("charge per unit: "))
print("*******************************************")

total_electricity_units = electricity_spend * charge_per_unit

output = (food + rent + total_electricity_units) // persons

print("Each person will pay = ", output)