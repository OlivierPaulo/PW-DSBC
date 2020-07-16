#import pprint
from time import sleep
from sys import exit

def printBoard(Board):
  print("Game Here" + "  Where to play")
  print("  -------" + "    -------")
  print(f"  |{Board['a']}|{Board['b']}|{Board['c']}|" + "    |a|b|c|")
  print("  -------" + "    -------")
  print(f"  |{Board['d']}|{Board['e']}|{Board['f']}|" + "    |d|e|f|")
  print("  -------" + "    -------")
  print(f"  |{Board['g']}|{Board['h']}|{Board['i']}|" + "    |g|h|i|")
  print("  -------" + "    -------")

def who_start():
  print("If you wanna start press 1 or if you let me start press 2 ? ",end="")
  turn = int(input())
  try : 
    if (turn == 1 or turn == 2):
      game(turn)
    else:
      who_start()
  except ValueError:
    print("Please choose 1 to start or 2 to let me start")
    who_start()

def game(turn):
  printBoard(Board)
  if check_win():
    exit()
  if turn % 2 == 0:
    ##computer turn
    print("\nMy turn :")
    if 'e' in possible():
      Board['e'] = "O"

    elif 'a' in possible () and ((Board['b'] == "O" and Board['c'] == "O") or ((Board['e'] == "O" and Board['i'] == "O")) or ((Board['d'] == "O" and Board['g'] == "O"))):
      Board['a'] = "O"
    elif 'c' in possible () and ((Board['a'] == "O" and Board['b'] == "O") or ((Board['g'] == "O" and Board['e'] == "O")) or ((Board['f'] == "O" and Board['i'] == "O"))):
      Board['c'] = "O"
    elif 'g' in possible () and ((Board['a'] == "O" and Board['d'] == "O") or ((Board['c'] == "O" and Board['e'] == "O")) or ((Board['h'] == "O" and Board['i'] == "O"))):
      Board['g'] = "O"
    elif 'i' in possible () and ((Board['a'] == "O" and Board['e'] == "O") or ((Board['c'] == "O" and Board['f'] == "O")) or ((Board['g'] == "O" and Board['h'] == "O"))):
      Board['i'] = "O"
    elif 'b' in possible () and ((Board['a'] == "O" and Board['c'] == "O") or ((Board['e'] == "O" and Board['h'] == "O"))):
      Board['b'] = "O"
    elif 'd' in possible () and ((Board['a'] == "O" and Board['g'] == "O") or ((Board['e'] == "O" and Board['f'] == "O"))):
      Board['d'] = "O"
    elif 'f' in possible () and ((Board['c'] == "O" and Board['i'] == "O") or ((Board['d'] == "O" and Board['e'] == "O"))):
      Board['f'] = "O"
    elif 'h' in possible () and ((Board['b'] == "O" and Board['e'] == "O") or ((Board['g'] == "O" and Board['i'] == "O"))):
      Board['h'] = "O"

    else:
      if 'a' in possible() and (((Board['b'] == "X") and (Board['c'] == "X")) or ((Board['d'] == "X") and (Board['g'] == "X")) or (((Board['e'] == "X") and (Board['i'] == "X")))):
        Board['a'] = "O"
    
      elif 'b' in possible() and (((Board['a'] == "X") and (Board['c'] == "X")) or ((Board['e'] == "X") and (Board['h'] == "X"))):
        Board['b'] = "O"
      
      elif 'c' in possible() and (((Board['a'] == "X") and (Board['b'] == "X")) or ((Board['e'] == "X") and (Board['g'] == "X")) or (((Board['f'] == "X") and (Board['i'] == "X")))):
        Board['c'] = "O"

      elif 'd' in possible() and (((Board['a'] == "X") and (Board['g'] == "X")) or ((Board['e'] == "X") and (Board['f'] == "X"))):
        Board['d'] = "O"

      elif 'f' in possible() and (((Board['d'] == "X") and (Board['e'] == "X")) or ((Board['c'] == "X") and (Board['i'] == "X"))):
        Board['f'] = "O"
      
      elif 'g' in possible() and (((Board['a'] == "X") and (Board['d'] == "X")) or ((Board['c'] == "X") and (Board['e'] == "X")) or (((Board['h'] == "X") and (Board['i'] == "X")))):
        Board['g'] = "O"

      elif 'h' in possible() and (((Board['b'] == "X") and (Board['e'] == "X")) or ((Board['g'] == "X") and (Board['i'] == "X"))):
        Board['h'] = "O"
      
      elif 'i' in possible():
        Board['i'] = "O"      

      else:
        if 'a' in possible():
          Board['a'] = "O"
        elif 'c' in possible():
          Board['c'] = "O"
        elif 'g' in possible():
          Board['g'] = "O"
        elif 'i' in possible():
          Board['i'] = "O"
        else:
          for move in possible():
            Board[move] = "O"
            break
        
    
  else:
    ##user turn
    print("\nYour turn :")
    print(f"choose where you put the X using letter : {comma(possible())}")
    choice = str(input())
    while choice not in possible():
      print(f"Choice : {choice} not possible. Please choose {comma(possible())}")
      choice = str(input()) 
    Board[choice] = "X"

  turn += 1
  game(turn)


def possible():
  move_available = []
  for k,v in Board.items():
    if v == ' ':
      move_available.append(k)
  return move_available

def comma(possible_move):
  sentence ="'"
  possible_move.sort(key=str.lower)
  for i in range(len(possible_move)):
      if i == len(possible_move)-1:
        sentence += "or "+ possible_move[i]
        break
      sentence += possible_move[i] + ", "

  sentence += "'"
  return sentence

def check_win():
  print("")
  if Board['a'] == 'X' and Board['b'] == 'X' and Board['c'] == 'X':
    print("Congrats, You Win !")
    return True
  elif Board['d'] == 'X' and Board['e'] == 'X' and Board['f'] == 'X':
    print("Congrats, You Win !")
    return True
  elif Board['g'] == 'X' and Board['h'] == 'X' and Board['i'] == 'X':
    print("Congrats, You Win !")
    return True
  elif Board['a'] == 'X' and Board['d'] == 'X' and Board['g'] == 'X':
    print("Congrats, You Win !")
    return True
  elif Board['b'] == 'X' and Board['e'] == 'X' and Board['h'] == 'X':
    print("Congrats, You Win !")
    return True
  elif Board['c'] == 'X' and Board['f'] == 'X' and Board['i'] == 'X':
    print("Congrats, You Win !")
    return True
  elif Board['a'] == 'X' and Board['e'] == 'X' and Board['i'] == 'X':
    print("Congrats, You Win !")
    return True
  elif Board['c'] == 'X' and Board['e'] == 'X' and Board['g'] == 'X':
    print("Congrats, You Win !")
    return True
  elif Board['a'] == 'O' and Board['b'] == 'O' and Board['c'] == 'O':
    print("Ooohhh, You Lose !")
    return True
  elif Board['d'] == 'O' and Board['e'] == 'O' and Board['f'] == 'O':
    print("Ooohhh, You Lose !")
    return True
  elif Board['g'] == 'O' and Board['h'] == 'O' and Board['i'] == 'O':
    print("Ooohhh, You Lose !")
    return True
  elif Board['a'] == 'O' and Board['d'] == 'O' and Board['g'] == 'O':
    print("Ooohhh, You Lose !")
    return True
  elif Board['b'] == 'O' and Board['e'] == 'O' and Board['h'] == 'O':
    print("Ooohhh, You Lose !")
    return True
  elif Board['c'] == 'O' and Board['f'] == 'O' and Board['i'] == 'O':
    print("Ooohhh, You Lose !")
    return True
  elif Board['a'] == 'O' and Board['e'] == 'O' and Board['i'] == 'O':
    print("Ooohhh, You Lose !")
    return True
  elif Board['c'] == 'O' and Board['e'] == 'O' and Board['g'] == 'O':
    print("Ooohhh, You Lose !")
    return True
  
  elif Board['a'] != ' ' and Board['b'] != ' ' and Board['c'] != ' ' and Board['d'] != ' ' and Board['e'] != ' ' and Board['f'] != ' ' and Board['g'] != ' ' and Board['h'] != ' ' and Board['i'] != ' ':
    print("It's a Tie !")
    return True
  else:
    return False


Board = {
  'a':' ',
  'b':' ',
  'c':' ',
  'd':' ',
  'e':' ',
  'f':' ',
  'g':' ',
  'h':' ',
  'i':' '
} 

who_start()


