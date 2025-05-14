from collections import deque 
 
initial_state = (0, 0, 0, 0)   
goal_state = (1, 1, 1, 1)     
 
def is_valid_state(state): 
    farmer, lion , goat, grass = state 
     
    if (lion == goat and goat != farmer) or (goat == grass and grass != 
farmer): 
        return False 
    return True 
 
def get_neighbors(state): 
    farmer, lion, goat, grass = state 
    neighbors = [] 
 
    possible_moves = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)] 
 
    for move in possible_moves: 
        lion_move, goat_move, grass_move = move 
 
        if farmer == 0:   
            new_farmer_pos = 1 
            new_lion = lion + lion_move 
            new_goat = goat + goat_move 
            new_grass = grass + grass_move 
        else:   
            new_farmer_pos = 0 
            new_lion = lion - lion_move 
            new_goat = goat - goat_move 
            new_grass = grass - grass_move 
 
         
        if not (0 <= new_lion <= 1 and 0 <= new_goat <= 1 and 0 <= 
new_grass <= 1): 
            continue 
 
        new_state = (new_farmer_pos, new_lion, new_goat, new_grass) 
        if is_valid_state(new_state): 
            neighbors.append(new_state) 
 
    return neighbors 
 
def bfs(): 
    queue = deque([(initial_state, [])]) 
    visited = set() 
    visited.add(initial_state) 
 
    while queue: 
        state, path = queue.popleft() 
 
        left_side = ["Farmer" if state[0]==0 else "", "Lion" if state[1] 
== 0 else "", "Goat" if state[2] == 0 else "", "Grass" if state[3] == 0 
else ""] 
        right_side = ["Farmer" if state[0]==1 else "", "Lion" if state[1] 
== 1 else "", "Goat" if state[2] == 1 else "", "Grass" if state[3] == 1 
else ""] 
 
        print(f"Starting Side: {', '.join(filter(None, left_side)) if 
any(left_side) else 'Empty'}") 
        print(f"Target Side: {', '.join(filter(None, right_side)) if 
any(right_side) else 'Empty'}") 
        print('-' * 40) 
 
        if state == goal_state: 
            return path + [state] 
 
        for neighbor in get_neighbors(state): 
            if neighbor not in visited: 
                visited.add(neighbor) 
                queue.append((neighbor, path + [state])) 
 
    return None 
 
solution = bfs() 
