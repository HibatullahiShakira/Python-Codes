to_continue = 'yes'
while to_continue ==  'yes':
	number_of_gallons = float(input("Enter the gallon used: "))
	miles_driven = float(input("Enter miles driven: "))
	miles_per_gallon = miles_driven / number_of_gallons
	print(f'The miles per gallon for this tank was: {miles_per_gallon:.2f}')
	to_continue = input("Enter yes or no to continue: ")
	
	