import random
import os

movesDone = 0

def create_board(size):
  '''int->list (of str)
  Precondition: size is even positive integer between 2 and 52
  '''
  board = [None]*size 
  letter='A'
  for i in range(len(board)//2):
    board[i]=letter
    board[i+len(board)//2 ]=board[i]
    letter=chr(ord(letter)+1)
  random.shuffle(board)
  return board
def print_board(a):
  '''(list of str)->None
  Prints the current board in a nicely formated way
  '''
  for i in a:
    print('{0:4}'.format(i), end=' ')
  print()
  for i in range(len(a)):
    print('{0:4}'.format(str(i+1)), end=' ')
  print()
def wait_for_player():
  '''(None)->None
  Pauses the program until the user presses enter
  '''
  print()
  try:
    input("Press enter to continue ")
  except SyntaxError:
    pass
def player_play(board, uncovered):
  '''
  (list of str, list of str) -> list of str

  This function takes the completely solved board in the list "board" and the already matched values in the "uncovered" list.
  The function then prompts the user to enter two number guesses, which then are checked to see if the two values selected are a match.
  If they are a match, permanently change them from an * to their true value. If g1 and g2 dont match, the values are uncovered temporarily, and waif for the user to press enter before continuing.

  there are no preconditions
  '''
  print()
  validresp = True
  while (validresp):
    try:
          g1 = int(input("Please enter two guesses:\n"))
          g2 = int(input())
          if (g1 < 1 or g1 > len(board) or g2 < 1 or g2 > len(board) or g1 == g2):
            print("Please enter valid numbers.")
          else:
            if uncovered[g1-1] == "*" and uncovered[g2-1] == "*":
              if board[g1-1] == board[g2-1]:
                uncovered[g1-1] = board[g1-1]
                uncovered[g2-1] = board[g2-1]
              else:
                uncovered[g1-1] = board[g1-1]
                uncovered[g2-1] = board[g2-1]
                resetTopBar()
                print_board(uncovered)
                wait_for_player()
                uncovered[g1-1] = '*'
                uncovered[g2-1] = '*'
              validresp = False
            else:
              print("One or both of the numbers you entered have already been uncovered. Try again.\n")
    except:
      print()
  return uncovered
def checkWin(bord):
  '''
  (list of str) -> bool

  this checks the list of already solved values in "bord" too see if there are any *'s.
  If there aren't any *'s, the function returns true, meaning the game is over and the player won.

  there are no preconditions
  '''
  win = True
  for x in bord:
    if x == "*":
      win = False
      break
  return win
def play_game(board, uncovered):
  '''
  (list of str, list of str)->int

  takes in the master board stored in the "board" variable, and the unsolved board in the "uncovered" variable. 
  It repeats asking the user to guess until the checkWin function returns true, which then exits the loop. 
  The function returns the count integer, which is how many moves it took for the player to solve the puzzle.

  there are no preconditions
  '''
  NotDone = True
  count = 0
  while (NotDone):
    os.system('cls')
    print_title()
    print_board(uncovered)
    uncovered = player_play(board, uncovered)
    NotDone = not checkWin(uncovered)
    count += 1
  resetTopBar()
  print("__     __          __          ___       _ \n\ \   / /          \ \        / (_)     | |\n \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |\n  \   / _ \| | | |   \ \/  \/ / | | '_ \| |\n   | | (_) | |_| |    \  /\  /  | | | | |_|\n   |_|\___/ \__,_|     \/  \/   |_|_| |_(_)\n                                           ")
  return count
def resetTopBar():
  '''
  (None) -> None

  The variable clears the console and redraws the title bar

  there are no preconditions
  '''
  os.system('cls')
  print_title()
def print_title():
  ''' 
  (None) -> None 
  
  Prints the Title bar of the program 
  
  there are no preconditions
  '''
  print("  __  __                                    ____                      \n |  \/  | ___ _ __ ___   ___  _ __ _   _   / ___| __ _ _ __ ___   ___ \n | |\/| |/ _ \ '_ ` _ \ / _ \| '__| | | | | |  _ / _` | '_ ` _ \ / _ \ \n | |  | |  __/ | | | | | (_) | |  | |_| | | |_| | (_| | | | | | |  __/\n |_|  |_|\___|_| |_| |_|\___/|_|   \__, |  \____|\__,_|_| |_| |_|\___|\n                                   |___/                              \n\n")
def Start():
  '''
  (None) -> None

  This function executes the main body of the program and asks the user to input a size, which it validates before creating a board of that size. The function also calculates the minimum number of mooves it could take, as well as displaying both the minimum and the ammount the user took to complete.

  There are no preconditions
  '''
  print_title()
  iseven = False
  while iseven == False:
    size = int(input("How many cards do you want to play with?\nEnter an even number between 2 and 52: "))
    if(size < 2 or size > 52):
      resetTopBar()
      print("Please enter a number within the range.")
      print()
    elif (size%2==0):
      iseven = True
    else:
      resetTopBar()
      print("Please enter an EVEN number.")
      print()

  board=create_board(size)
  uncovered = ['*']*size
  movesDone = play_game(board, uncovered)
  print("The game could've been completed in a total of", str(round(size/2)), "moves.")
  print("You completed the challenge in", str(movesDone), "moves.")

Start()

waitforend = input()
