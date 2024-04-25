def string_addition(character):

	if len(character) < 3:
		return character

	if  character.endswith("ing"):
		return character + "ly"
		
	else: 
		return character + "ing"
	

print(string_addition("addly"))	