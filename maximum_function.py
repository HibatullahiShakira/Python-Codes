def maximum(*numbers):
	maximum_value = numbers[0]
	
	for number in numbers:
		if number > maximum_value:
			maximum_value = number
	return maximum_value 


print(maximum(2,3,4,5))