print("Rock..")
print("Paper...")
print("Scissors....")
st_player = input("First player: Rock, Scissors or Paper? ")
print("****DON'T LOOK ABOVE****\n\n" * 40)
nd_player = input("Second player: Rock, Scissors or Paper? ")
st_player = st_player.lower()
nd_player = nd_player.lower()
if st_player == nd_player:
	print("It's a tie")
elif st_player == "scissors" and nd_player == "rock":
	print("The second player wins")
elif st_player == "rock" and nd_player == "paper":
	print("The second player wins")
elif st_player == "paper" and nd_player == "rock":
	print("The first player wins")
elif st_player == "rock" and nd_player == "scissors":
	print("The first player wins")
elif st_player == "paper" and nd_player == "scissors":
	print("The second player wins")
elif st_player == "scissors" and nd_player == "paper":
	print("The first player wins")
else:
	print("Something went wrong")