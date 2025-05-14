#initially: (farmer, lion, goat, grass) 
initial_state = (0, 0, 0, 0)  # all on left side 
goal_state = (1, 1, 1, 1)     # all on right side 
possible_moves = [(1, 0, 0, 0), (1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1)]  # 
Farmer always moves with one of these items or alone 
 
def is_valid_state(state): 
  Farmer, Lion, Goat, Grass = state 
  if (Lion == Goat and Goat != Farmer) or (Goat == Grass and Grass != Farmer): 
    return False 
  return True 
 
def get_neighbors(state): 
  neighbors = [] 
  Farmer, Lion, Goat, Grass = state 
 
  for move in possible_moves: 
    new_farmer = 1 - Farmer  # Farmer always moves to the opposite side 
    new_lion   = Lion   if move[1] == 0 else new_farmer 
    new_goat   = Goat   if move[2] == 0 else new_farmer 
    new_grass  = Grass  if move[3] == 0 else new_farmer 
 
    new_state = (new_farmer,new_lion,new_goat,new_grass) 
    if is_valid_state(new_state): 
      # Append both the new state and the move taken (action). 
      neighbors.append((new_state, move)) 
 
  return neighbors 
 
def dfs(): 
  stack = [(initial_state,[])] # list "stack" containing tuples of (state,path 
keep track of all the paths to reach current "state") 
  visited = [] 
  visited.append(initial_state) 
 
  while stack: 
    state,path = stack.pop() #path keep track of all the paths to reach current 
"state" 
 
    left_side = ["Farmer" if state[0]==0 else "","Lion" if state[1]==0 else "", 
"Goat" if state[2]==0 else "", "Grass" if state[3]==0 else ""] 
    right_side = ["Farmer" if state[0]==1 else "","Lion" if state[1]==1 else "", 
"Goat" if state[2]==1 else "", "Grass" if state[3]==1 else ""] 
 
print(f"Starting Side: {', '.join(filter(None, left_side)) if any(left_side) 
else 'Empty'}") 
print(f"Target Side: {', '.join(filter(None, right_side)) if any(right_side) 
else 'Empty'}") 
print('-' * 40) 
if state == goal_state: 
return path + [state] 
for neighbor, move in get_neighbors(state): 
if neighbor not in visited: 
visited.append(neighbor) 
#  
Store both the new state and the move taken (path) between states. 
stack.append((neighbor, path + [(state, move)]))  # Store the new_state 
and the path 
return None 
solution = dfs()
