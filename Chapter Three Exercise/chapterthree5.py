INTEREST_RATE = 7
PERCENTAGE = 100
interest_rate_decimal = 7 / 100
amount = int(input("Enter Amount: "))
year = int(input("Enter year: "))
for number in range(1, year + 1):
	annual_interest = amount * interest_rate_decimal
	amount += annual_interest 
	print(f"The amount on deposit at the of year {number} is {amount:.2f} ")
	