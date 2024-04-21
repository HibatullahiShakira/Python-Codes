number = int(input('Enter number: '))

i = 1
while (i > number):
	i = i + 1 
	
if (number % 2 == 0):
	print(number, 'is even number')
else: 
	print(number, 'is odd number')
	i = i + 1
	
	