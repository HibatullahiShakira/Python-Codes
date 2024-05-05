def vowels_consonants(words):
	vowels = ['a','e','i','o', 'u']
	vowel = 0
	consonant = 0
	
	for i in words:
		#for vowels in words:
		if i in vowels:
			vowel += 1 
		else:
			if i not in vowels:
				consonant += 1


	return f'consonants: {consonant} vowels: {vowel}'		

print(vowels_consonants("academy"))
 