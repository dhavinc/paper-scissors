print("Rock..")
print("Paper...")
print("Scissors....")
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
		print("The second player wins")
		replay = input("You want to play again? If yes press 'y', if not press 'n': ")
		if(replay=='y'):
			st_player = None
			nd_player = None
		else:
			print("Thank you for playing")
			break
	elif st_player == "rock" and nd_player == "paper":
		print("The second player wins")
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
		print("The second player wins")
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