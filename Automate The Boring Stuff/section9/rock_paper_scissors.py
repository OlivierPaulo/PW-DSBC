from random import choice

def main():
  choice_list = ['rock','paper','scissors']
  computer_choice = choice(choice_list)

  print("Hey, let's play Rock, Paper and Scissors :)")
  print("Please make your choice : ")
  user_choice = input()
  
  check_user_choice(user_choice,computer_choice,choice_list)

  print("Play again ? (y for Yes, q for Quit)")
  play_again(input())
    
def play_again(play):
  if play == "y":
    print("Yeah, let's play again :)")
    main()

  elif play == "q":
    print("Ok. Have a nice day !")
    exit()

  else:
    print(f"Your choice was not clear :s : {play}, y for Yes or q for Quit")
    play_again(input())

def check_user_choice(user_choice,computer_choice,choice_list):
  
  if user_choice.lower() in choice_list:
    game(user_choice,computer_choice)
  else:
    print(f"Your choice is not valid. Please choose between Rock, Paper or Scissors ? :")
    user_choice = input()
    check_user_choice(user_choice,computer_choice,choice_list)
    
def game(user_choice,computer_choice):

  print(f"Computer Choice is : {computer_choice.capitalize()}")
  print(f"Your Choice is : {user_choice.capitalize()}")
  u_choice = user_choice.lower()
  c_choice = computer_choice.lower()
  
  if u_choice == "rock":
    if c_choice == "scissors":
      print(f"You win as {u_choice.capitalize()} wins against {c_choice.capitalize()} !")
    elif c_choice == "paper" :
      print(f"You lose as {u_choice.capitalize()} loses against {c_choice.capitalize()} !")
    else:
      print(f"It's a draw !")
  
  elif u_choice == "paper":
    if c_choice == "rock":
      print(f"You win as {u_choice.capitalize()} wins against {c_choice.capitalize()} !")
    elif c_choice == "scissors" :
      print(f"You lose as {u_choice.capitalize()} loses against {c_choice.capitalize()} !")
    else:
      print(f"It's a draw !")

  else:
    if c_choice == "paper":
      print(f"You win as {u_choice.capitalize()} wins against {c_choice.capitalize()} !")
    elif c_choice == "rock" :
      print(f"You lose as {u_choice.capitalize()} loses against {c_choice.capitalize()} !")
    else:
      print(f"It's a draw !")
      
main()



