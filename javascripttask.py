def range_value(*numbers):
	
	max_value = numbers[0]
	min_value = numbers[0]
	for number in numbers:
		if number < min_value:
			min_value = number
		if number > max_value:
			max_value = number
	return max_value - min_value




print(range_value(7,4,2,3,4))
