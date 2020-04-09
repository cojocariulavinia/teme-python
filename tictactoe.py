# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

# Display the game board to the screen
def display_board():
    print(board[0]+ "|" + board[1] + "|" + board[2])
    print(board[3]+ "|" + board[4] + "|" + board[5])
    print(board[6]+ "|" + board[7] + "|" + board[8])


# lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
winner = None

# Whos turn is it
current_player = "X"

def play_game():

  #Show the initial game board
  display_board()

  #Loop until the game stops
  while game_still_going:

    #Handle Turn
    handle_turn(current_player)

    # Check if th game is over
    check_if_game_over()

    # Flip to the other player
    flip_player()

  # Since the game is over, print the winner or tie
  if winner == "X"  or winner == "O":
    print(winner + " won!")
  elif winner == None:
    print("It's a tie!")

# Handle a turn for an arbritrary player
def handle_turn(player):
  
  #Get position from player
  print (player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input and the spot is open 
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
     position = input("Invalid input. Choose a position from 1-9!")

    position = int(position) - 1

    # Make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Try again.")

  #Put the game piece on the  board
  board[position] = player
  display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
  #set up global variables
  global winner 
  row_winner = check_rows()    
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  if row_winner:
    winner =  row_winner
  elif column_winner:
    winner = colums_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
    
def check_rows():
  # set up global variables
  global game_still_going 
  #check if any of the rows have all the same value
  row_1 = board[0] == board[1] == board[2] !="-"
  row_2 = board[3] == board[4] == board[5] !="-"
  row_3 = board[6] == board[7] == board[8] !="-"
  #if any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner(X or O)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  else:
      return None

def check_columns():
  # set up global variables
  global game_still_going 
  #check if any of the columns have all the same value
  column_1 = board[0] == board[3] == board[6] !="-"
  column_2 = board[1] == board[4] == board[7] !="-"
  column_3 = board[2] == board[5] == board[8] !="-"
  #if any column does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner(X or O)
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  else:
      return None

def check_diagonals():
  # set up global variables
  global game_still_going 
  #check if any of the diagonals have all the same value
  diagonal_1 = board[0] == board[4] == board[8] !="-"
  diagonal_2 = board[6] == board[4] == board[2] !="-"
  #if any diagonal does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Return the winner(X or O)
  if diagonal_1:
    return board[0]

  elif diagonal_2:
    return board[2]
  else:
      return None

def check_if_tie():
  # Set global variables
  global game_still_going
  if "-" not in board:
    game_still_going = False
    return True
  else:
    return False

def flip_player():
  #global variables needed
  global current_player
  #if the current player was X, change it to O
  if current_player == "X":
    current_player = "O"
    #if the current player was O, change it to X
  elif current_player == "O":
    current_player = "X"
    return
    
play_game()




