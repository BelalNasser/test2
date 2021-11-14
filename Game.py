import random as rd
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_game = [rock,paper,scissors]
val= int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer = rd.randint(0,len(list_game)-1)
if val == computer:
  print(list_game[val])
  print("Computer chose: \n\n"+ list_game[computer] )
  print("It's a draw\n")
  
elif list_game[val] == rock and list_game[computer] == paper:
  print(list_game[val])
  print("Computer chose: \n\n"+ list_game[computer] )
  print("Computer Win !")

elif list_game[val] == paper and list_game[computer]==rock:
      print(list_game[val])
      print("Computer chose: \n\n")
      print(list_game[computer] )
      print("You Win!\n")
      
elif list_game[val] == rock and list_game[computer] == scissors:
  print(list_game[val])
  print("Computer chose: \n\n"+ list_game[computer] )
  print("You win!\n")
  
  
elif list_game[val] == scissors and list_game[computer] == rock:
  
  print(list_game[val])
  print("Computer chose: \n\n")
  print(list_game[computer] )
  print("Computer win  !\n")
  
  
elif list_game[val] == paper and list_game[computer] == scissors:
  print(list_game[val])
  print("Computer chose: \n\n")
  print(list_game[computer] )
  print("Computer Win !") 
  

elif list_game[val] == scissors and list_game[computer] == paper:
  print(list_game[val])
  print("Computer chose: \n\n"+ list_game[computer] )
  print("You Win!\n")
  
  