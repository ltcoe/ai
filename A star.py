import heapq
import itertools

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def calculate_heuristic(self):
        # Manhattan distance heuristic
        h = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    target_row, target_col = divmod(self.state[i][j] - 1, 3)
                    h += abs(i - target_row) + abs(j - target_col)
        return h

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_valid_move(i, j):
    return 0 <= i < 3 and 0 <= j < 3

def is_goal_state(state):
    return state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def get_possible_moves(state):
    i, j = get_blank_position(state)
    possible_moves = []
    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if is_valid_move(x, y):
            new_state = [list(row) for row in state]
            new_state[i][j], new_state[x][y] = new_state[x][y], new_state[i][j]
            possible_moves.append((new_state, (x, y)))
    return possible_moves

def print_solution(node):
    if node is not None:
        print_solution(node.parent)
        if node.move:
            print(f"Move {node.move} =>")
        for row in node.state:
            print(row)
        print("\n")

def solve_puzzle(initial_state):
    start_node = PuzzleNode(initial_state)
    open_list = [start_node]
    closed_set = set()

    while open_list:
        current_node = heapq.heappop(open_list)

        if is_goal_state(current_node.state):
            print("Solution Found:")
            print_solution(current_node)
            return

        closed_set.add(tuple(tuple(row) for row in current_node.state))

        for next_state, move in get_possible_moves(current_node.state):
            next_node = PuzzleNode(next_state, current_node, move, current_node.cost + 1)
            if tuple(tuple(row) for row in next_node.state) not in closed_set:
                heapq.heappush(open_list, next_node)

    print("No solution found")
def get_user_input():
    print("Enter the initial state of the 8-puzzle:")
    initial_state = []
    for i in range(3):
        row = input(f"Enter row {i + 1} (use spaces between numbers): ").split()
        if len(row) != 3:
            print("Invalid input. Please enter 3 numbers per row.")
            return None
        initial_state.append([int(num) for num in row])
    return initial_state

def main():
    initial_state = get_user_input()
    if initial_state is not None:
        solve_puzzle(initial_state)

if __name__ == "__main__":
    main()
