def is_palindrome(character):
	number_in_reverse = ""
	if type(character) in [int, float]:
		return False
	for i in range (len(character)-1,-1,-1):
		number_in_reverse += character[i]
	return character == number_in_reverse


