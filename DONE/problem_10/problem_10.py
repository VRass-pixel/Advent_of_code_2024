MOVES = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


def parse_input(file: str):
    with open(file, 'r') as f:
        lines = f.readlines()
    
    return [list(map(int, lines[i].strip())) for i in range(len(lines))]


def part_a(file: str)  -> int:
    map = parse_input(file)

    def get_a_nine(row: int, col: int, seen: set) -> int:
        for move in MOVES:
            new_row = row + MOVES[move][0]
            new_col = col + MOVES[move][1]

            if new_row < 0 or new_row >= len(map) or new_col < 0 or new_col >= len(map[new_row]):
                continue
            
            prev_value = map[row][col]
            new_value  = map[new_row][new_col]

            if new_value - prev_value == 1:
                if new_value == 9:
                    seen.add((new_row, new_col))
                    continue

                get_a_nine(new_row, new_col, seen=seen)

        return

    trailheads = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == 0:
                seen = set()
                get_a_nine(row=row, col=col, seen=seen)
                trailheads += len(seen)

    return trailheads


def part_b(file: str) -> int:
    map = parse_input(file)

    def get_a_nine(row: int, col: int) -> int:
        nines = 0
        for move in MOVES:
            new_row = row + MOVES[move][0]
            new_col = col + MOVES[move][1]

            if new_row < 0 or new_row >= len(map) or new_col < 0 or new_col >= len(map[new_row]):
                continue
            
            prev_value = map[row][col]
            new_value  = map[new_row][new_col]

            if new_value - prev_value == 1:
                if new_value == 9:
                    nines += 1
                    continue

                nines += get_a_nine(new_row, new_col)

        return nines

    ratings = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == 0:
                ratings += get_a_nine(row=row, col=col)

    return ratings

if __name__ == '__main__':

    file = 'problem_10/input_10.txt'

    part_a_sol = part_a(file)
    print(f'Part A: {part_a_sol}')

    part_b_sol = part_b(file)
    print(f'Part B: {part_b_sol}')