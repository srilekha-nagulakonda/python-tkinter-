import random
print("Winning rules of the Rock, Paper, Scissor game as follow:\n " + "Rock v/s Paper\n" + "Rock v/s Scissor\n" + "Paper v/s Scissor\n")
while True:
  print("Enter choice \n 1 for Rock,\n 2 for Paper, \n 3 for Scisssor")
  choice = int(input("User turn :"))
  while choice > 3 or choice < 1 :
    choice = int(input("Enter valid input :"))
  if choice == 1:
    choice_name = 'Rock' 
  elif choice == 2:
    choice_name = 'Paper'
  else:
    choice_name = 'Scissor'
  print("User choice is :" + choice_name)
  
  print(" Now Computer turn : ")
  computer_choice = random.randint(1,3)
  while computer_choice == choice:
     computer_choice = random.randint(1,3)
  if  computer_choice == 1:
      computer_choice_name = 'Rock'
  elif  computer_choice == 2:
      computer_choice_name = 'Paper'
  else:
      computer_choice_name = 'Scissor'
  print(" computer choice is :" + computer_choice_name)
  print( choice_name + "V/S" + computer_choice_name)
  if choice == computer_choice:
    print("Draw =>" , end="")
    result = "Draw"
  if ((choice == 1 and computer_choice==2) or (choice == 2 and computer_choice==1)):
    print("Paper wins =>",end="")
    result = "paper" 
  elif ((choice == 1 and computer_choice==3) or (choice == 3 and computer_choice==1)):
    print("Rock wins =>",end="")
    result = "Rock"
  else:
    print("Scissor wins =>",end="")
    result = "scissor"
  if result == "Draw":
    print("Its a Tie")
  if result == choice_name :
    print("User Win")
  else:
    print("Computer win")
  print("Do you want to play again ? (y/n)")
  ans = input().lower
  if ans == 'n':
    break
print("\n Thanks for playing")    