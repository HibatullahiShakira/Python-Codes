positive = 1
negative = 0
count = 1
user_input = int(input("Enter number: "))
while user_input != 0:
	user_input = int(input("Enter number: "))
	if user_input < 0:
		negative += 1

	if user_input > 0:
		positive = positive + 1
	count +=1
print(f"The positive numbers are {positive} \nThe negative numbers are {negative}")
print(f"Total numbers entered: {count}")
					

			
				
				
			