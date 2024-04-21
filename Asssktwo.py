smallest_number = None
largest_number = None
while True:
	user_input = int(input("Enter number: "))
	if largest_number is None or user_input > largest_number:
		largest_number = user_input
	elif smallest_number is None or user_input < smallest_number:
		smallest_number = user_input
	to_continue = int(input("To continue enter 0 and to exit enter -1: "))
if to_continue == -1:
	print("program exited")
break
	print(f"the largest of the number is {largest_number}")
	print(f"the smallest of the number is {largest_number}")
	