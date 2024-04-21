result = 1
sum = 0
for number in range(4, 11, 4):
	if(number % 4 == 0):
		for j in range(1, 6):
			result = number ** j
			#print(result)
			sum += result
			print(sum)
			
