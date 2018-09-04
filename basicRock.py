import random
print("Rock..")
print("Paper...")
print("Scissors....")
while True:
	choice = input("VS Human type 1, VS Machine type 2: ")
	choice = int(choice)
	if(choice == 1 or choice == 2):
		break
if(choice==1):
	st_player = None
	nd_player = None
	while True:
		st_player = input("First player: Rock, Scissors or Paper? ")
		print("****DON'T LOOK ABOVE****\n\n" * 40)
		nd_player = input("Second player: Rock, Scissors or Paper? ")
		st_player = st_player.lower()
		nd_player = nd_player.lower()
		if st_player == nd_player:
			print("It's a tie")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				nd_player = None
			else:
				print("Thank you for playing")
				break
		elif st_player == "scissors" and nd_player == "rock":
			print("Computer wins")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				nd_player = None
			else:
				print("Thank you for playing")
				break
		elif st_player == "rock" and nd_player == "paper":
			print("Computer wins")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				nd_player = None
			else:
				print("Thank you for playing")
				break
		elif st_player == "paper" and nd_player == "rock":
			print("The first player wins")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				nd_player = None
			else:
				print("Thank you for playing")
				break
		elif st_player == "rock" and nd_player == "scissors":
			print("The first player wins")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				nd_player = None
			else:
				print("Thank you for playing")
				break
		elif st_player == "paper" and nd_player == "scissors":
			print("Computer wins")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				nd_player = None
			else:
				print("Thank you for playing")
				break
		elif st_player == "scissors" and nd_player == "paper":
			print("The first player wins")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				nd_player = None
			else:
				print("Thank you for playing")
				break
		else:
			print("Something went wrong")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				nd_player = None
			else:
				print("Thank you for playing")
				break
else:
	st_player = None
	computer = None
	while True:
		random_num = random.randint(0,3)
		if(random_num==0):
			computer="Rock"
		if(random_num==1):
			computer="Scissors"
		else:
			computer="Paper"
		st_player = input("First player: Rock, Scissors or Paper? ")
		st_player = st_player.lower()
		computer = computer.lower()
		if st_player == computer:
			print("It's a tie")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				computer = None
			else:
				print("Thank you for playing")
				break
		elif st_player == "scissors" and computer == "rock":
			print("Computer wins")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				computer = None
			else:
				print("Thank you for playing")
				break
		elif st_player == "rock" and computer == "paper":
			print("Computer wins")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				computer = None
			else:
				print("Thank you for playing")
				break
		elif st_player == "paper" and computer == "rock":
			print("The first player wins")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				computer = None
			else:
				print("Thank you for playing")
				break
		elif st_player == "rock" and computer == "scissors":
			print("The first player wins")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				computer = None
			else:
				print("Thank you for playing")
				break
		elif st_player == "paper" and computer == "scissors":
			print("Computer wins")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				computer = None
			else:
				print("Thank you for playing")
				break
		elif st_player == "scissors" and computer == "paper":
			print("The first player wins")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				computer = None
			else:
				print("Thank you for playing")
				break
		else:
			print("Something went wrong")
			replay = input("You want to play again? If yes press 'y', if not press 'n': ")
			if(replay=='y'):
				st_player = None
				computer = None
			else:
				print("Thank you for playing")
				break