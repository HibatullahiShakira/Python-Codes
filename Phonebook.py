def menu():
	while(True):
		print("List of menu functions")
		print("""
		0. Exit
		1. Phonebook
		2. Messages
		3. Chat
		4. Call register
		5. Tones
		6. Settings
		7. Call divert 
		8. Games
		9. Calculator
		10. Reminders
		11. Clock
		12. profiles
		13. SIM services
		""")

	option = int(input("Press Menu of choice:   "))

	match option: 



			case 1: 
				phonebook
			case 2:
				Messages
			case 3: 
				Chat menu
			case 4:
				Call register
			case 5:
				Tone
			case 6: 
				Settings
			case 7:
				Call divert
			case 8: 
				Games
			case 9:
				Calculator
			case 10:
				Reminders
			case 11:
				Clock
			case 12:
				profiles
			case 13:
				Sim_Services
			case 0: 
				print("Exiting the menu.")
				break
			case _:
				print("Invalid option, please try again.")



			
	case 1: 
		phonebook

		while(True):
			print("""
			1. Search 
			2. Services Nos.
			3. Add name
			4. Erase
			5. Edit
			6. Assign tone 
			7. Send b'card 
			8. Options
			9. Speed dials
			10. Voice tags
			""")
		
			int(input("Press Menu of choice:   "))

			match option:
		
				case 1: 
					Search
				case 8: 
					Options
				case 0:
					break
				case _:
					print("invalid option, please try again.")
	
while(True):
	print("""
	1. Write messages
	2. Inbox
	3. Outbox
	4. Picture messages
	5. Templates
	6. Smileys
	7. Messages Settings
	8. Info Services 
	9. Voice mailbox number
	10. Service command editor
	""")
	option = int(input("Press Menu of choice:   "))
	match option:
		case 1: 
			Write messages
		case 7: 
			Message Settings
		case 0:
			break
		case _:
			print("invalid option, please try again.")
		

while(True):
	print("""
	1. Set 1
	2. Common
	""")
	int(input("Press Menu of choice:   "))
	match option:
		case 1:
			Set 1
		case 2:
			Commom
		case 0:
			break
		case _:
			print("invalid option, please try again.")

while(True):
	print("""
	1. Message centre number
	2. Message sent as
	3. Message validity
	""")
	int(input("Press Menu of choice:   "))


while(True):
	print("""
	1. Delivery reports
	2. Reply via same centre
	3. Character support
	""")
	int(input("Press Menu of choice:   "))


while(True):
	print("""
	1. Missed calls 
	2. Received calls
	3. Dialled calls
	4. Erase recent call lists
	5. Show call durations
	6. Show call costs
	7. Call costs settings
	8. Prepaid Credit 
	""")
	int(input("Press Menu of choice:   "))
	match option:
		case 1: 
			Missed calls
		case 5:
			Show call durations
			case 6:
				Show call cost
			case 7:
				Callcost settings
			case 0:
				break
			case _:
				print("invalid option, please try again.")


while(True):
	print("""
	1. Last call duration
	2. All call's duration
	3. Received calls
	4. Dialled calls duration
	5. Clear timers	
	""")
	int(input("Press Menu of choice:   "))	



while(True):
	print("""
	1.List call cost
	2. All call's cost
	3. Clear counters
	""")
	int(input("Press Menu of choice:   "))	


while(True):
	print("""
	1. Call cost limit 
	2. Show costs in
	""")
	int(input("Press Menu of choice:   "))	





		
			





							


			