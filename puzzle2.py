# Program by Prithviraj Arvind Pawar
# Puzzle assignment 2 Happy Cows Farm


import random
from queue import Queue
import copy
import sys

field = []
temp = []
q = Queue()
inputFile = sys.argv[1]
outputFile = sys.argv[2]

class Cow(object):


# reading input file
    with open(inputFile) as f:
        lines = f.readlines()
       
        for i in lines:
            a = list(i.rstrip())
            field.append(a)
   
    size_of_field = int(field[0][0]) #takes out size of farm from input.txt file
    ##print(size_of_field)

#counting number of @'s
    z = "@"
    counter = 0
    for i in range(len(field)):
        counter += field[i].count(z)
    i = 1 





#to find index of Character in this case for "C"

def find(char):
    for i, istr in enumerate(field):
        
        for j,jstr in enumerate(istr):
            try:
                if jstr == char:
                    yield i, j
            except ValueError:
                continue

# to check if the index is outofbounds     
       
def isValidPos(i, j, n, m):
 
    if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
        return 0
    return 1

# to calculate score

def CountScore(arr, i, j):
    offsets = [[-1,-1],[-1,0],[-1,1],
               [0,-1],        [0, 1],
               [ 1,-1],[1, 0],[1,1]]

    
 # Size of given 2d array
    n = len(arr)
    m = len(arr[0])

    CowScore = 0
    another_cow = False
    pond = False
    haystack = False
    for off in range(0,8):
        
        row = i + offsets[off][0] # 1 + [-1]
        col = j + offsets[off][1]
        
        
        
        total = sum(offsets[off])
        
        if total == -1 or total == 1:
            orthogonal = True
        else:
            orthogonal = False
        
        
        if (isValidPos(row,col,n,m)):
            if arr[row][col] == 'C':
                another_cow = True
            elif orthogonal:
                if arr[row][col] == '@':
                    haystack = True
                if arr[row][col] == '#':
                    pond = True
   
    if another_cow:
        CowScore -= 3
    if haystack:
        CowScore += 1
        if pond:
           CowScore += 2
    
    return CowScore

# to generate output file

def output_data(lines, filename):
    with open(filename, 'w') as file:
        for item in field:
            for i in range(len(item)):
                file.write("%s" % item[i])
            file.write("\n")
        file.close()

#replacing "." with "C"

#for i in q.queue:
#    for j in i:
#        if field[j[0]][j[1]] == ".":
#            temp = field
#            temp[j[0]][j[1]] = "C"
#            af_q.put(temp)
#    print("this is field :" , field)
#    print("this is af_q" , af_q.queue)

# takes the field map from the input text file
farm_grid = field[1:]

# pops the first element in input text file 
farmSize = field.pop(0)

# generating frontier
for i in range(0,int(farmSize[0])):
   for j in range(0,int(farmSize[0])):
       q.put([(i,j)])
               
##print("this is queue",q.queue)

# Runs the loop when frontier is not empty 
# Uses BFS algorithm
while not q.empty():
   ## print(q.queue)

# getting action states from forntier
    action_state = q.get()

# initializing total score of the game
    Total_Cow_Score = 0

# creates temporary copy of farm
    temp = copy.deepcopy(farm_grid)

    ##print("this is action :",action_state)
  
# replaces grass with cow based on action state
    for i in action_state :
        row = i[0]
        col = i[1]

        if temp[row][col] == ".":
            temp[row][col] = "C"

# for calculating total score of game
    for i in action_state :
        row = i[0]
        col = i[1]

        Total_Cow_Score += CountScore(temp, row, col)

# finds the smallest path for the require score 
    if Total_Cow_Score >= 7:
        field = temp[:]
        print(f"The frontier is {action_state}")
        break

    for i in range(0, int(farmSize[0])):
        for j in range(0, int(farmSize[0])):
                temp_action = action_state[:]
                if (i,j) > action_state[-1] and farm_grid[i][j] == '.':
                    temp_action.append((i,j))
                    q.put(temp_action)


#Find the index for all the Cows placed in the farm
matches = [match for match in find('C')]

#Calculate Score of all the cows
Total_Cow_Score = 0
for i,j in matches:
    Total_Cow_Score += CountScore(field, i, j)

#Adds total score to array
field.append([str(Total_Cow_Score)])

#Adds farm size back to array
field.insert(0, farmSize)

#creates outputfile
output_data(field,outputFile)



