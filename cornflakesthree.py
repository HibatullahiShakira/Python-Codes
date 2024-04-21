passed = 0
failed = 0
for number in range(15):
	scores = int(input("Enter Scores: "))
	if scores >= 45:
		passed += 1
	elif scores < 45:
		failed += 1
print(f"The total number of student that failed is {failed} \nThe total number of student that passed is {passed}")