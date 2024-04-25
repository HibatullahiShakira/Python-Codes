def character_return(character):
	if len(character) < 2: 
		return '""'
	else:
		return character[:2] + character[-2:]




print(character_return("o"))