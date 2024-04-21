while True:			
	number = int(input("Enter number: "))
	number1 = int(input("Enter number: "))
	total = number + number1
	print(total)
	to_continue = int(input("To continue enter 0 and to exit enter -1: "))
	if to_continue == -1:
		print("program exited")
		break
		