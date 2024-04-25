def even_indexes_character(character):
	result = ''
	for i in range(1, len(character), 2):
		result += character[i]
	return result

print(even_indexes_character("semicolon"))