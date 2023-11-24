from itertools import permutations

def is_solvable(puzzle):
    inversions = 0
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] > puzzle[j] and puzzle[i] != 0 and puzzle[j] != 0:
                inversions += 1
    return inversions % 2 == 0
def solve_puzzle(initial_state):
    if not is_solvable(initial_state):
        print("Puzzle is not solvable.")
        return
    goal_state = tuple(range(9))
    for permuted_state in permutations(initial_state):
        if permuted_state == goal_state:
            print("Solution found:")
            print_puzzle(list(permuted_state))
            return
    print("Solution not found.")
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

if __name__ == "__main__":
    initial_state = [1, 2, 0, 4, 5, 3, 7, 8, 6]
    solve_puzzle(initial_state)
