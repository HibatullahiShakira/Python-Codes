sum = 0
product = 1
numbers = []
for number in range(4):
	number = int(input("Enter number: "))
	numbers.append(number)
	sum += number 
	product *= number
	maximum = max(numbers)
	minimum = min(numbers)
average = sum / 4
print(f"The product of the numbers is: {product} \nThe sum of the numbers are: {sum} \nThe average of the numbers is: {average} \nThe maximun of the numbers is: {maximum} \nThe minimum of the numbers is: {minimum}")