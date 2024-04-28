RATE = 20
amount = int(input("Enter amount: "))
year = int(input("Enter year: "))
percentage_rate = RATE / 100
for number in range(year):
	interest_calculation = amount * percentage_rate
	print(interest_calculation)
