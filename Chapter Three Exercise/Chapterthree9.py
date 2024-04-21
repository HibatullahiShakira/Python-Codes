sum = 1
for i in range(1, 10 + 1):
	factorial = 1
	for j in range(1, i):
		factorial *= j
	e = 1 / factorial
	sum += e
	print(sum)
