#Stage-2 Tic-Tac-Toe program

row0 = ["-", "-", "-"]
row1 = ["-", "-", "-"]
row2 = ["-", "-", "-"]

#Function to print tic_tac board
def print_board():
  print("Printing board")
  print(row0)
  print(row1)
  print(row2)
  print("")

#Calling the function print_board
print_board()


#Takes the arguments row and col and returns a True if a mark can be placed at the row and col on the board otherwise False
def check_mark(row, col):
  if row < 0 or row > 2:
    print("Invalid row number. It has to be 0, 1 or 2")
    return (False)
  elif col < 0 or col > 2:
    print("Invalid column number. It has to be 0, 1 or 2")
    return (False)
  else:
    return (True)


#Takes the arguments row ,col and player_id and places a “X” at the row, col if player_id is 1 and a “O” if player_id is 2
def place_mark(row, col, player_id):
  if player_id == 1:
    if row == 0:
      if row0[col] == "-":
        row0[col] = "X"
      else:
        print("This row and column already filled")
        return False
    elif row == 1:
      if row1[col] == "-":
        row1[col] = "X"
      else:
        print("This row and column already filled")
        return False
    elif row == 2:
      if row2[col] == "-":
        row2[col] = "X"
      else:
        print("This row and column already filled")
        return False
  else:
    if row == 0:
      if row0[col] == "-":
        row0[col] = "O"
      else:
        print("This row and column already filled")
        return False
    elif row == 1:
      if row1[col] == "-":
        row1[col] = "O"
      else:
        print("This row and column already filled")
        return False
    elif row == 2:
      if row2[col] == "-":
        row2[col] = "O"
      else:
        print("This row and column already filled")
        return False

#Function to check the winner
def check_win(player_id):
  if player_id == 1:
    check = "X"
  else:
    check = "O"
  if ((row0[0] == check and row0[1] == check and row0[2] == check) or
    (row1[0] == check and row1[1] == check and row1[2] == check) or
    (row2[0] == check and row2[1] == check and row2[2] == check) or
    (row0[0] == check and row1[0] == check and row2[0] == check) or
    (row0[1] == check and row1[1] == check and row2[1] == check) or
    (row0[2] == check and row1[2] == check and row2[2] == check) or
    (row2[0] == check and row1[1] == check and row0[2] == check) or
    (row0[0] == check and row1[1] == check and row2[2] == check)):
    return True
  else:
    return False

winner = 0
check = False

player_id = 1

for i in range(0,9):
  if (i%2 == 0):
    player_id = 1
  else:
    player_id = 2

  while check == False:
    print("Player", player_id)
    #Reading row and column numbers from user
    row = int(input("Enter row number: "))
    col = int(input("Enter column number: "))

    #Calling check_mark
    check = check_mark(row, col)
  
    #Calling place_mark
    check = place_mark(row, col, player_id)

  print_board()

  if check_win(player_id) == True:
    winner = 1
    print("Player", player_id, "is the winner !!")
    break
  else:
    check = False

if winner == 0:
  print("Neither player won")