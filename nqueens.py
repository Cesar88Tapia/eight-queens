BOARD_SIZE = 8

#Function to define risks within the queens
def under_attack(column, existing_queens):
  #Define if queen exists within the row, if not add one      
  row = len(existing_queens) + 1
  #Iterate through the existing queens     
  for queen in existing_queens:
  #Define the queen position 
    r, c = queen
    if r == row: return True #Checking row
    if c == column: return True #Checking column
    if(column - c) == (row - r): return True #Check if it's diagonal left
    if(column - c) == -(row - r): return True #Check if it's diagonal right
  return False
  
