def longest_word(*characters):
	longest = characters[0]

	for character in characters:
		if len(character) > len(longest):
			longest = character

	return f" {longest} \n {len(longest)}"

print(longest_word('welcome', 'out', 'weather', 'mobile', 'breakfast', 'journey'))
