while(True):
	print("The Twelves Days of Christmas")
	print("Song by the Wiggles")

	print( """
	1 -> First day
	2 -> Second day
	3 -> Third day 
	4 -> Fourth day
	5 -> Fifth day
	6 -> Sixth day 
	7 -> seventh day
	8 -> Eight day
	9 -> Nineth day
	10 -> Tenth day
	11 -> Eleventh day 
	12 -> Twelveth day
	""")


	option = int(input("Press Day of chioce between 1 to 12: "))

	match option:

		case 1:
			print("""
			First day
			On the first day of christmas
			my true love gave to me
			A patridge in a pear tree.
			""")

		case 2: 
			print("""
			Second day
			On the second day of christmas
			my true love gave to me
			Two turtle doves
			A patridge in a pear tree.
			""")
		case 3:
			print("""
			Third day
			On the third day of christmas,
			my true love gave to me
			Three french hens
			Two turtle doves
			A patridge in a pear tree.
			""")
		case 4:
			print("""
			Fourth day
			On the fourth day of christmas,
			my true love gave to me
			Three french hens
			Two turtle doves
			And a patridge in a pear tree.
			""")		
		case 5: 
			print("""
			Fifth day
			On the fifth day of christmas,
			my true love gave to me,
			Five golden rings,
			Three French hens,
			Two turtle doves,
			And a patridge in a pear tree.
			""")		
		case 6: 
			print("""
			Sixth day
			On the sixth day of christmas,
			my true love gave to me,
			Six geese a-laying,
			Five golden rings,
			Four calling birds,
			Three French hens,
			Two turtle doves,
			And a patridge in a pear tree.
			""")
		case 7:
			print("""
			Seventh day
			On the seventh day of christmas,
			my true love gave to me
			Seven swans a-swimming,
			Six geese a-laying,
			Five golden rings,
			Four calling birds,
			Three French hens,
			Two turtle doves,
			And a patridge in a pear tree.	
			""")	
		case 8: 
			print("""
			Eighth day
			On the Eighth day of christmas,
			my true love gave to me,
			Eight maids a-milking,
			Seven swans a-swimming,
			Six geese a-laying,
			Five golden rings,
			Four calling birds,
			Three French hens,
			Two turtle doves,
			And a patridge in a pear tree.
			""")		
							
		case 9:
			print("""
			Nineth day
			On the Nineth day of christmas,
			my true love gave to me,
			Nine ladies dancing,
			Eight maids a-milking,
			Seven swans a-swimming,
			Six geese a-laying,
			Five golden rings,
			Four calling birds,
			Three French hens,
			Two turtle doves,
			And a patridge in a pear tree.
			""")			

		case 10:
			print("""
			Tenth day
			On the Tenth day of christmas,
			my true love gave to me,
			Ten lords a-leaping,
			Nine ladies dancing,
			Eight maids a-milking,
			Seven swans a-swimming,
			Six geese a-laying,
			Five golden rings,
			Four calling birds,
			Three French hens,
			Two turtle doves,
			And a patridge in a pear tree.
			""")						
		case 11:
			print("""
			Eleventh day
			On the Eleventh day of christmas,
			my true love gave to me,
			Eleven pipers piping,
			Ten lords a-leaping,
			Nine ladies dancing,
			Eight maids a-milking,
			Seven swans a-swimming,
			Six geese a-laying,"
			Five golden rings,
			Four calling birds,
			Three French hens,
			Two turtle doves,
			And a patridge in a pear tree.		
			""")
						
		case 12:
			print("""
			Twelveth day
			On the Twelveth day of christmas,
			Twelve drummers drumming
			my true love gave to me,
			Eleven pipers piping,
			Ten lords a-leaping,
			Nine ladies dancing,
			Eight maids a-milking,
			Seven swans a-swimming,
			Six geese a-laying,
			Five golden rings,
			Four calling birds,
			Three French hens,
			Two turtle dove,
			And a patridge in a pear tree.
			""")
		case _:
			print("end of lyrics")
	if option == 0:
			print("lyrics ended")
			break

					

