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
  
  #Create function to find solutions
def solve(n):
  #If n is equal to 0 return empty array for no solution
  if n == 0: return [[]]
  #Fucntions for smaller solutions
  smaller_solutions = solve(n-1)
  #Store solutions in array
  solutions = []
  #Iterate through solutions in smaller solutions
  for solution in smaller_solutions:
    #Iterate through colum´s range in the board size and increment by one
    for column in range(1, BOARD_SIZE + 1):
      #If there is no risk place queen
      if not under_attack(column, solution):
        solutions.append(solution + [(n, column)])
        #Return solutions
  return solutions

#Create function to display solutions
def display(solution):
  chars = list()
  #Iterate through row range in board size
  for r in range(BOARD_SIZE):
    #Iterate through colum range in board size
    for c in range(BOARD_SIZE):
      #If queen does not conflict
      if (r + 1, c + 1) in solution:
        #Place one to list
        chars.append("1 ")
      else:
        #If it does conflict place 0
        chars.append("0 ")
    if r != BOARD_SIZE:
      chars.append("\n")
  return ("".join(chars))
  
for answer in solve(BOARD_SIZE): 
  print(display(answer) + "\n\n")
