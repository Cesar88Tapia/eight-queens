solutions = []

#Create a function to define if given position is threatened by another queen
def threatened(pos, past, n):
    #Iterate through past positions
    for i in range(len(past)):
        #If last position conflicts
        if past[i] == pos or abs(pos - past[i]) == len(past) - i:
            #Return ture
            return True
    #Otherwise return false
    return False

#Create function to identify positions of queens
def nqueens(n, past=None):
    #If there is no threat(no previous position)
    if past == None:
        #Generate first positions
        return [nqueens(n, [i+1]) for i in range(n)]
    #If we find solution
    if len(past) == n:
        #Store the solution into solutions
        solutions.append(past)
        #Else find more solutions and keep storing solutions if there is no threat
    else:
        [nqueens(n, past + [pos]) for pos in range(1, n+1) if not threatened(pos, past, n)]

nqueens(8) # replace 8 with arbitrary n
print(len(solutions))

## solutions is now a list of all solutions for n number of queens

#if n is 4, prints 2, if n is 8, prints 92, etc
