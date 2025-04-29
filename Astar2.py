practical2
#Implement A star Algorithm for any game search problem


import heapq

def print_board(state):
    for i in range(9):
        if i % 3 == 0:
            print()
        print("_" if state[i] == -1 else state[i], end=" ")
    print()

def is_solvable(start):
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

def manhattan_distance(state, goal):
    h = 0
    for i in range(9):
        if state[i] == -1:
            continue
        goal_index = goal.index(state[i])
        h += abs(i // 3 - goal_index // 3) + abs(i % 3 - goal_index % 3)
    return h

def get_neighbors(state):
    neighbors = []
    pos = state.index(-1)
    row, col = pos // 3, pos % 3

    def swap_and_store(new_pos):
        new_state = state[:]
        new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]
        neighbors.append(new_state)

    if col > 0:
        swap_and_store(pos - 1)
    if col < 2:
        swap_and_store(pos + 1)
    if row > 0:
        swap_and_store(pos - 3)
    if row < 2:
        swap_and_store(pos + 3)

    return neighbors

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start, goal), 0, start))
    came_from = {}
    g_score = {tuple(start): 0}
    visited = set()

    while open_set:
        _, cost, current = heapq.heappop(open_set)
        current_t = tuple(current)

        if current == goal:
            path = reconstruct_path(came_from, current_t)
            print("\nSolved!")
            for state in path:
                print_board(state)
                print()
            print(f"Number of moves: {len(path) - 1}")
            return

        visited.add(current_t)

        for neighbor in get_neighbors(current):
            neighbor_t = tuple(neighbor)
            tentative_g = g_score[current_t] + 1

            if neighbor_t in visited and tentative_g >= g_score.get(neighbor_t, float('inf')):
                continue

            if tentative_g < g_score.get(neighbor_t, float('inf')):
                came_from[neighbor_t] = current_t
                g_score[neighbor_t] = tentative_g
                f_score = tentative_g + manhattan_distance(neighbor, goal)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))

    print("No solution found.")

# ========== MAIN ==========
def main():
    print("Enter the start state (use -1 for empty space):")
    start = []
    while len(start) < 9:
        row = list(map(int, input(f"Row {len(start) // 3 + 1} (3 values): ").split()))
        if len(row) != 3:
            print("Please enter exactly 3 numbers.")
            continue
        start.extend(row)

    print("Enter the goal state (use -1 for empty space):")
    goal = []
    while len(goal) < 9:
        row = list(map(int, input(f"Row {len(goal) // 3 + 1} (3 values): ").split()))
        if len(row) != 3:
            print("Please enter exactly 3 numbers.")
            continue
        goal.extend(row)

    print("\nStart State:")
    print_board(start)

    print("\nGoal State:")
    print_board(goal)

    if is_solvable(start):
        a_star(start, goal)
    else:
        print("The given puzzle is not solvable.")

if __name__ == "__main__":
    main()

Output:

Enter the start state (use -1 for empty space):     
Row 1 (3 values): 1 2 3 
Row 2 (3 values): 4 -1 6
Row 3 (3 values): 7 5 8 
Enter the goal state (use -1 for empty space):
Row 1 (3 values): 1 2 3 
Row 2 (3 values): 4 5 6 
Row 3 (3 values): 7 8 -1

Start State:

1 2 3
4 _ 6
7 5 8

Goal State:

1 2 3
4 5 6
7 8 _

Solved!

1 2 3
4 _ 6
7 5 8


1 2 3
4 5 6
7 _ 8


1 2 3
4 5 6
7 8 _

Number of moves: 2

   





