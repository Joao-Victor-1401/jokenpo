import random
computer = random.randrange(1,3)
ppt = int(input("1. Rock 2. Paper 3. Scissors -> "))
if ppt == computer:
  print("Draw")
elif ppt == 1 and computer == 2:
  print("Computer win")
elif ppt == 1 and computer == 3:
  print("You win")
elif ppt == 2 and computer == 1:
  print("You win")
elif ppt == 2 and computer == 3:
  print("Computer win")
elif ppt == 3 and computer == 1:
  print("Computer win")
elif ppt == 3 and computer == 2:
  print("You win")
else:
	print("Invalid Number")