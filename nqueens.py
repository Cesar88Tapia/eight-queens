solutions = []

#Create a function to define position and last position in the board
def threatened(pos, past, n):
    #Iterate through the length of last positions
    for i in range(len(past)):
        #If last position conflicts
        if past[i] == pos or abs(pos - past[i]) == len(past) - i:
            #Return ture
            return True
    #Otherwise return false
    return False

def nqueens(n, past=None):
    if past == None:
        return [nqueens(n, [i+1]) for i in range(n)]
    if len(past) == n:
        solutions.append(past)
    else:
        [nqueens(n, past + [pos]) for pos in range(1, n+1) if not threatened(pos, past, n)]

nqueens(8)
print(len(solutions))
