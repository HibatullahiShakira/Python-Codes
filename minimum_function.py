def minimum(*numbers):
	minimum_value = numbers[0]
	
	for number in numbers:
		if number < minimum_value:
			minimum_value = number
	return minimum_value 


print(minimum(2,3,4,5))