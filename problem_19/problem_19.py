from functools import lru_cache


def parse_input(file: str) -> list:
    with open(file, 'r') as f:
        lines = f.readlines()

    get_patterns = True
    designs = []
    for line in lines:
        line = line.strip()
        if get_patterns:
            patterns = tuple(sorted(line.split(', '), key=len, reverse=True))
            get_patterns = False

        else:
            if line == '':
                continue
            designs.append(line)

    return patterns, designs



@lru_cache(maxsize=None)
def search(pattern, towels):
    design_count = 0
    for towel in towels:
        if pattern == towel:
            design_count += 1

        if pattern.startswith(towel):
            design_count += search(pattern.removeprefix(towel), towels)

    return design_count


def part_a(file: str)  -> int:
    towels, patterns = parse_input(file)

    valid_designs = 0
    for pattern in patterns:
        valid_designs += (search(pattern, towels) > 0)

    return valid_designs

def part_b(file: str)  -> int:
    towels, patterns = parse_input(file)

    valid_designs = 0
    for pattern in patterns:
        valid_designs += search(pattern, towels)

    return valid_designs

if __name__ == '__main__':

    file = 'problem_19/input_19.txt'

    part_a_sol = part_a(file)
    print(f'Part A: {part_a_sol}')

    part_b_sol = part_b(file)
    print(f'Part B: {part_b_sol}')