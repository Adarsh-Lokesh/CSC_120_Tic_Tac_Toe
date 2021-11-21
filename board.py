row0 = ["-", "-", "-"]
row1 = ["-", "-", "-"]
row2 = ["-", "-", "-"]

#Function to print tic_tac board
def print_board():
  print("Printing board")
  print(row0)
  print(row1)
  print(row2)

#Calling the function print_board
print_board()


#Takes the arguments row and col and returns a True if a mark can be placed at the row and col on the board otherwise False
def check_mark(row, col):
  if row < 0 or row > 2:
    print("Invalid row number. It has to be 0, 1 or 2")
  elif col < 0 or col > 2:
    print("Invalid column number. It has to be 0, 1 or 2")
  else:
    print(" ")


#Takes the arguments row ,col and player_id and places a “X” at the row, col if player_id is 1 and a “O” if player_id is 2
def place_mark(row, col, player_id):
  if player_id == 1:
    if row == 0:
      if row0[col] == "-":
        row0[col] = "X"
      else:
        print("This row and column already filled")
    elif row == 1:
      if row1[col] == "-":
        row1[col] = "X"
      else:
        print("This row and column already filled")
    elif row == 2:
      if row2[col] == "-":
        row2[col] = "X"
      else:
        print("This row and column already filled")
  else:
    if row == 0:
      if row0[col] == "-":
        row0[col] = "O"
      else:
        print("This row and column already filled")
    elif row == 1:
      if row1[col] == "-":
        row1[col] = "O"
      else:
        print("This row and column already filled")
    elif row == 2:
      if row2[col] == "-":
        row2[col] = "O"
      else:
        print("This row and column already filled")

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
     print("Winner")
     return(1)

for i in range(0,9):
  #Reading row and column numbers from user
  row = int(input("Enter row number: "))
  col = int(input("Enter column number: "))
  #Reading player id
  player_id = int(input("Enter player id: "))

  #Calling check_mark
  check_mark(row, col)

  #Calling place_mark
  place_mark(row, col, player_id)

  print_board()

  if check_win(player_id) == 1:
    break;