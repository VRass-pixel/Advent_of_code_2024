from dataclasses import dataclass
import heapq
from itertools import combinations


def parse_input(file: str) -> list:
    with open(file, 'r') as f:
        lines = f.readlines()

    map = []
    for line in lines:
        line = line.strip()
        if 'E' in line:
            goal = (line.index('E'), len(map))
        if 'S' in line:
            orig = (line.index('S'), len(map))
        
        map.append(list(line))

    return map, orig, goal

MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Down, Up, Right, Left

@dataclass
class Node:
    pos: tuple
    cost: int
    parent: 'Node' = None

    def __lt__(self, other):
        return self.cost < other.cost
    
def heuristic(node: Node, goal: Node) -> int:
    return abs(node.pos[0] - goal.pos[0]) + abs(node.pos[1] - goal.pos[1])

def a_star(map_, orig, goal, get_path=False, break_if_cost=float('inf')):
    orig_node = Node(pos=orig, cost=0)
    goal_node = Node(pos=goal, cost=0)

    # Priority queue for open list
    open_list = []
    heapq.heappush(open_list, (heuristic(orig_node, goal_node), orig_node))

    visited_cost = {}  # Tracks minimum cost at which each node was visited

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node.cost > break_if_cost:
            break

        # Goal check
        if current_node.pos == goal_node.pos:
            cost = current_node.cost
            if get_path:
                path = []
                while current_node:
                    path.append(current_node.pos)
                    current_node = current_node.parent
                return path[::-1], cost
            return None, cost

        # Add to visited with its cost
        if current_node.pos in visited_cost and visited_cost[current_node.pos] <= current_node.cost:
            continue
        visited_cost[current_node.pos] = current_node.cost

        # Explore neighbors
        for delta_x, delta_y in MOVES:
            new_x = current_node.pos[0] + delta_x
            new_y = current_node.pos[1] + delta_y

            # Check bounds and obstacles
            if new_x < 0 or new_x >= len(map_[0]) or new_y < 0 or new_y >= len(map_) or map_[new_y][new_x] == '#':
                continue

            new_cost = current_node.cost + 1  # Assuming uniform cost for moves
            new_node = Node(pos=(new_x, new_y), cost=new_cost, parent=current_node)

            # Skip if already visited with a lower or equal cost
            if new_node.pos in visited_cost and visited_cost[new_node.pos] <= new_cost:
                continue

            priority = new_cost + heuristic(new_node, goal_node)
            heapq.heappush(open_list, (priority, new_node))

    return None, float('inf')  # No path found

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def part_b(file: str)  -> int:
    map, orig, goal = parse_input(file)

    path, _ = a_star(map, orig, goal, get_path=True)

    distances = {orig: 0} 
    for i in range(1, len(path)):
        distances[path[i]] = distances[path[i-1]] + 1

    total_improves = 0
    for (point_a, cost_a), (point_b, cost_b) in combinations(distances.items(), 2):
        delta = distance(point_a, point_b)
        if delta < 21 and cost_b - cost_a - delta >= 100:
            total_improves += 1
                
    return total_improves

def part_a(file: str)  -> int:
    map, orig, goal = parse_input(file)

    path, _ = a_star(map, orig, goal, get_path=True)

    distances = {orig: 0} 
    for i in range(1, len(path)):
        distances[path[i]] = distances[path[i-1]] + 1

    total_improves = 0
    for (point_a, cost_a), (point_b, cost_b) in combinations(distances.items(), 2):
        delta = distance(point_a, point_b)
        if delta == 2 and cost_b - cost_a - delta >= 100:
            total_improves += 1

                
    return total_improves

if __name__ == '__main__':

    file = 'problem_20/input_20.txt'

    part_a_sol = part_a(file)
    print(f'Part A: {part_a_sol}')

    part_b_sol = part_b(file)
    print(f'Part B: {part_b_sol}')