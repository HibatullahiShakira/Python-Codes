import random

WINNING_NUMBER = random.randrange(1,10);

user_input = int(input("Enter number from 1 to 10: "))

while WINNING_NUMBER != user_input :
	user_input = int(input("Enter number from 1 to 10: "))
	
	if  user_input == WINNING_NUMBER: 
		print("Congratulations you guessed right")
		break
	else:
		print("You guessed wrong")