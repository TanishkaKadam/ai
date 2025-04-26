practical2
#Implement A star Algorithm for any game search problem

def print_board(elements):
    for i in range(9):
        if i % 3 == 0:
            print()
        print("_" if elements[i] == -1 else elements[i], end=" ")
    print()

def solvable(start):
    inv = 0
    for i in range(9):
        if start[i] == -1:
            continue
        for j in range(i + 1, 9):
            if start[j] == -1:
                continue
            if start[i] > start[j]:
                inv += 1
    return inv % 2 == 0

def heuristic(start, goal):
    h = 0
    for i in range(9):
        if start[i] == -1:
            continue
        goal_index = goal.index(start[i])
        h += abs(i // 3 - goal_index // 3) + abs(i % 3 - goal_index % 3)
    return h

def move(start, position, direction):
    new_state = start[:]
    if direction == 'left':
        new_state[position], new_state[position - 1] = new_state[position - 1], new_state[position]
    elif direction == 'right':
        new_state[position], new_state[position + 1] = new_state[position + 1], new_state[position]
    elif direction == 'up':
        new_state[position], new_state[position - 3] = new_state[position - 3], new_state[position]
    elif direction == 'down':
        new_state[position], new_state[position + 3] = new_state[position + 3], new_state[position]
    return new_state

def solveEight(start, goal, visited, move_count):
    if start == goal:
        print_board(start)
        print(f"Solved in {move_count} moves")
        return True

    visited.add(tuple(start))
    empty_pos = start.index(-1)
    row, col = empty_pos // 3, empty_pos % 3
    directions = []

    if col > 0: directions.append('left')
    if col < 2: directions.append('right')
    if row > 0: directions.append('up')
    if row < 2: directions.append('down')

    best_heuristic = float('inf')
    best_move = None
    best_state = None

    for direction in directions:
        new_state = move(start, empty_pos, direction)
        if tuple(new_state) not in visited:
            h = heuristic(new_state, goal)
            if h < best_heuristic:
                best_heuristic = h
                best_move = direction
                best_state = new_state

    if best_move:
        print_board(best_state)
        visited.add(tuple(best_state))
        return solveEight(best_state, goal, visited, move_count + 1)
    return False

def main():
    start = []
    goal = []

    print("Enter the start state (9 numbers, use -1 for empty space):")
    while len(start) < 9:
        try:
            row = list(map(int, input(f"Enter row {len(start)//3 + 1} (3 numbers): ").split()))
            if len(row) != 3:
                print("Please enter exactly 3 numbers.")
                continue
            start.extend(row)
        except ValueError:
            print("Invalid input. Please enter integers.")

    print("Enter the goal state (9 numbers, use -1 for empty space):")
    while len(goal) < 9:
        try:
            row = list(map(int, input(f"Enter row {len(goal)//3 + 1} (3 numbers): ").split()))
            if len(row) != 3:
                print("Please enter exactly 3 numbers.")
                continue
            goal.extend(row)
        except ValueError:
            print("Invalid input. Please enter integers.")

    print("Start State:")
    print_board(start)

    print("Goal State:")
    print_board(goal)

    if solvable(start):
        visited = set()
        if not solveEight(start, goal, visited, 0):
            print("No solution found.")
    else:
        print("Not possible to solve")

if __name__ == '__main__':
    main()


output :
tanishka@tanishka-Latitude-5490:~$ python3 astar2.py
Enter the start state (9 numbers, use -1 for empty space):
Enter row 1 (3 numbers): 3 7 6 
Enter row 2 (3 numbers): 5 1 2
Enter row 3 (3 numbers): 4 -1 8
Enter the goal state (9 numbers, use -1 for empty space):
Enter row 1 (3 numbers): 5 3 6
Enter row 2 (3 numbers): 7 -1 2
Enter row 3 (3 numbers): 4 1 8
Start State:

3 7 6 
5 1 2 
4 _ 8 
Goal State:

5 3 6 
7 _ 2 
4 1 8 

3 7 6 
5 _ 2 
4 1 8 

3 _ 6 
5 7 2 
4 1 8 

_ 3 6 
5 7 2 
4 1 8 

5 3 6 
_ 7 2 
4 1 8 

5 3 6 
7 _ 2 
4 1 8 

5 3 6 
7 _ 2 
4 1 8 
Solved in 5 moves
tanishka@tanishka-Latitude-5490:~$ 

