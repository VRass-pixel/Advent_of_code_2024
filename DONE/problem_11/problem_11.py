import functools


def parse_input(file: str):
    with open(file, 'r') as f:
        lines = f.read()
    
    return lines.strip().split(' ')


@functools.lru_cache(maxsize=None)  # to avoid computing the same function multiple times (with the same params)
def apply_rules(stone: str, blink_count: int, target_blinks: int) -> int:
    digits = len(stone)

    if blink_count == target_blinks:
        return 1
    
    n_stones = 0

    if stone == '0':
        n_stones += apply_rules('1', blink_count+1, target_blinks) 

    elif digits % 2 == 0:
        left_half = str(int(stone[:digits // 2]))
        right_half = str(int(stone[digits // 2:]))
        n_stones += apply_rules(left_half, blink_count+1, target_blinks)
        n_stones += apply_rules(right_half, blink_count+1, target_blinks)

    else:
        stone = str(int(stone) * 2024)
        n_stones += apply_rules(stone, blink_count+1, target_blinks)

    return n_stones

def part_a(file: str, target_blinks: int = 25)  -> int:
    stones = parse_input(file)

    return sum([apply_rules(stone, blink_count=0, target_blinks=target_blinks) for stone in stones])


if __name__ == '__main__':

    file = 'problem_11/input_11.txt'

    part_a_sol = part_a(file, target_blinks=25)
    print(f'Part A: {part_a_sol}')

    part_b_sol = part_a(file, target_blinks=75)
    print(f'Part B: {part_b_sol}')