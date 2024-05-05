def maximum_number(first_number, second_number, third_number):
	maximum = 0
	if first_number > maximum:
		maximum = first_number
	if second_number > maximum:
		maximum = second_number
	if third_number > maximum:
			maximum = third_number
	return maximum

def minimum_number(first_number, second_number, third_number):
	minimum = 0
	if first_number < minimum:
		minimum = first_number
	if second_number < minimum:
		minimum = second_number
	if third_number < minimum:
			minimum = third_number
	return minimum

print(minimum_number(2,6,8))

