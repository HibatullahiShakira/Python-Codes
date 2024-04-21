year = 0
RATE = 20 
amount = int(input("Enter amount: "))
year = int(input("Enter year: "))
percentage_rate = RATE / 100
for number in range(1, year + 1):
	interest_calculation = amount * percentage_rate
	amount += interest_calculation 
	print(f"Total interest at year {number} is {amount:.2f}")
