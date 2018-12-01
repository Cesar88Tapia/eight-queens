BOARD_SIZE = 8
        
def under_attack(column, existing_queens):
  row = len(existing_queens) + 1
  for queen in existing_queens:
    r, c = queen
    if r == row: return True #Checking row
    if c == column: return True #Checking column
    if(column - c) == (row - r): return True #Check if it's diagonal left
    if(column - c) == -(row - r): return True #Check if it's diagonal right
  return False
  
def solve(n):
  if n == 0: return [[]]
  smaller_solutions = solve(n-1)
  solutions = []
  for solution in smaller_solutions:
    for column in range(1, BOARD_SIZE + 1):
      if not under_attack(column, solution):
        solutions.append(solution + [(n, column)])
  return solutions

def display(solution):
  chars = list()
  for r in range(BOARD_SIZE):
    for c in range(BOARD_SIZE):
      if (r + 1, c + 1) in solution:
        chars.append("1 ")
      else:
        chars.append("0 ")
    if r != BOARD_SIZE:
      chars.append("\n")
  return ("".join(chars))
  
for answer in solve(BOARD_SIZE): 
  print(display(answer) + "\n\n")
