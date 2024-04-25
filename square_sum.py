def square_sum(*numbers):
	total = 0
	for number in numbers:
		square = number **2
		total += square
	return total


print(square_sum(2,3,4,5,7))