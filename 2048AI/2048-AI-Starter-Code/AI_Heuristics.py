import numpy as np, math
from copy import deepcopy
smoothWeight = 0.5
monoWeight  = 1.0
emptyWeight  = 2.7

def heuristics(grid, num_empty):
  '''
  This function scores the grid based on the algorithm implemented
  so that the maximize function of AI_Minimax can decide which branch
  to follow.
  '''
  grid = np.array(grid)
  max_val = 0
  max_r, max_c = 0, 0
  large_tile_penalty = 0
  for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] >= max_val:
            max_val = grid[i][j]
            max_r = i
            max_c = j
  large_tile_penalty = (6 - max_r - max_c)# + math.log(max_val)/15


  monolr = 0
  for i in range(len(grid)):
    for j in range(len(grid[i]) - 1):
      if(grid[i][j] > grid[i][j + 1]):
        monolr -= 1# + (math.log(grid[i][j] + 1) + math.log(grid[i][j + 1] + 1))/1000
      elif(grid[i][j] < grid[i][j + 1]):
        monolr +=  1# + (math.log(grid[i][j] + 1) + math.log(grid[i][j + 1] + 1))/1000
   # check that it's increasing from top to bottom
  monotd = 0
  for i in range(len(grid)):
    for j in range(len(grid[i]) - 1):
      if(grid[j][i] > grid[j + 1][i]):
        monotd -= 1# + (math.log(grid[j][i] + 1) + math.log(grid[j + 1][i] + 1))/1000
      elif(grid[j][i] < grid[j + 1][i]):
        monotd += 1# + (math.log(grid[j][i] + 1) + math.log(grid[j + 1][i] + 1))/1000
        
  # check smoothness
  smoothness = 0
  # check that it's smooth from left to right
  for i in range(len(grid)):
    for j in range(len(grid[i]) - 1):
      if(grid[i][j] == grid[i][j + 1]):
        smoothness += 1

  # check that it's smooth from top to bottom
  for i in range(len(grid)):
    for j in range(len(grid[i]) - 1):
      if(grid[j][i] == grid[j + 1][i]):
        smoothness += 1
        
  return (monoWeight * (monolr + monotd)) - (max(5, math.log(max_val,3)) * large_tile_penalty) + (smoothWeight * smoothness) + (emptyWeight * num_empty)

  # TODO: Implement your heuristics here. 
  # You are more than welcome to implement multiple heuristics
  
  # Weight for each score