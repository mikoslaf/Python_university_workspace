
from random import choice, randint


def generate_map(file_name: str, n_rows: int, n_cols: int,min_terrain_level: int, max_terrain_level: int):
    lines = []
    for _ in range(n_rows):
        ln = [str(randint(min_terrain_level, max_terrain_level)) for _ in range(n_cols)]
        lines.append(' '.join(ln) + '\n')
    lines[-1] = lines[-1][:-1]

    with open(file_name, 'w') as f:
        f.writelines(lines)

def load_board(file_name: str):
    board = []
    with open(file_name, 'r+') as f:
        for ln in f.readlines():
            row = [int(x) for x in ln.split(' ')]
            board.append(row)
    return board


def show_board(board: list[list[int]]):
    for row in board:
        print(' '.join([str(i) for i in row]))


def find_cheapest_left_to_right(board: list[list[int]]) -> tuple[int, int]:
    """
    Finds the lowest cost of crossing the board along a row, from left to right

    :param board:
    :return: tuple: (minimal_cost, row_number)
    """
    lista = [sum(board[x]) for x in range(len(board))]
    result_cost = min(lista)
    result_row = lista.index(result_cost)
    return (result_cost, result_row)

def find_cost_of_path(board: list[list[int]], path: list[tuple[int, int]]) -> int:
    """
    Finds the cost of the `path` on the `board` provided
    :param board:
    :param path:
    :return: cost of moving along the path
    """
    return sum([board[val[0]][val[1]] for val in path])

def get_possible_next_locations(current_locatoin: tuple[int,int], n_rows: int, n_cols: int) -> list[tuple[int,int]]:
    x, y = current_locatoin
    check_locatoin = [(x + 1, y),(x, y + 1),(x - 1, y),(x, y - 1)]
    return [x for x in check_locatoin if x[0] >= 0 and x[0] <= n_rows and x[1] >= 0 and x[1] <= n_cols]

def walk_the_landscape(board: list[list[int]], n_steps, acceptable_terrain_cost: int):
    n_rows = len(board)
    n_cols = len(board[0])
    visited = set()
    visited.add((0, 0))
    visited_ = []
    visited_.append((0, 0))

    for step in range(n_steps):
        at = choice(visited_)
        next_locations = get_possible_next_locations(at, n_rows, n_cols)
        for n_loc in next_locations:
            if n_loc in visited:
                continue

            if board[n_loc[0]][n_loc[1]] > acceptable_terrain_cost:
                continue

            print(f'visiting {n_loc}')
            visited.add(n_loc)
            visited_.append(n_loc)

    for x, y in visited:
        board[x][y] = 0

# pobrać kod z GitHuba'a

if __name__ == '__main__':
    import os

    print(f'starting in {os.getcwd()}')
    a: list[list[int]] = [[]]

    generate_map(file_name="test_lanscape.txt", n_rows=7, n_cols=20, min_terrain_level=0, max_terrain_level=9)
    #board1 = load_board('lanscape_1.txt')
    # print(board1)
    #show_board(board1)
    #print(find_cost_of_path(board1, [(0, 0), (0, 1), (0, 2), (1, 2)]))  # 12()
    #print(walk_the_landscape(board=board1))