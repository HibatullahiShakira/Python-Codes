print("WELCOME BACK TO SENDER LOGISTICS SERVICES")
riders_name = input("Enter riders name: ")
another_rider = 'yes'
collectionRate1 = 160
collectionRate2 = 200
collectionRate3 = 250
collectionRate4 = 500
base = 5000
while another_rider.lower() ==  'yes':
	sucessful_delivery = float(input("Enter the number of sucessful delivery: "))
	if sucessful_delivery <= 49 :
		result = sucessful_delivery * collectionRate1 + base
		print(f"\n{riders_name} wage for the day is {result:.2f}")

	elif sucessful_delivery <= 59 :
		result1 = sucessful_delivery * collectionRate2 + base
		print(f"\n{riders_name} wage for the day is {result1:.2f}")

	elif sucessful_delivery <= 69 :
		result2 = sucessful_delivery * collectionRate3 + base
		printf(f"\n{riders_name} wage for the day is {result2:.2f}")

	elif sucessful_delivery >= 70 :
		result3 = sucessful_delivery * collectionRate4 + base
		print(f"\n{riders_name} wage for the day {result3:.2f}")

	another_rider = input("Would you like to enter another riders name? (enter yes or no) ").strip().lower()

	