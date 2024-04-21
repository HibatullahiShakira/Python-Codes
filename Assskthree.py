user_input = int(input("Enter number: "))
factorial = 1
for number in range(1, user_input + 1):
	factorial = factorial * number
print(factorial)
