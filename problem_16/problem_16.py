def a_star(map, orig, goal, return_if_cost_exceeds=None):
    orig_node = Node(pos=orig, ori=0, cost=0)
    goal_node = Node(pos=goal, ori=0, cost=0)
    
    # a-star
    open_list = []
    heapq.heappush(open_list, (heuristic(orig_node, goal_node), orig_node))
    visited = set()

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node.pos == goal_node.pos:
            path = []
            cost = current_node.cost
            while current_node:
                path.append(current_node.pos)
                current_node = current_node.parent
            return path[::-1], cost

        for i in range(4):
            delta_x, delta_y = MOVES[i]
            new_x = current_node.pos[0] + delta_x
            new_y = current_node.pos[1] + delta_y

            if new_x < 0 or new_x >= len(map[0]) or new_y < 0 or new_y >= len(map) or map[new_y][new_x] == '#':
                continue

            changes_in_ori = min(abs(current_node.ori - i), 4 - abs(current_node.ori - i))
            cost = current_node.cost + 1 + 1_000 * changes_in_ori
            
            # Check if we should exceed cost limit
            if return_if_cost_exceeds is not None and cost > return_if_cost_exceeds:
                continue
            
            new_node = Node(pos=(new_x, new_y), ori=i, cost=cost, parent=current_node)

            if new_node.pos in visited:
                continue

            priority = cost + heuristic(new_node, goal_node)
            heapq.heappush(open_list, (priority, new_node))

        visited.add(current_node.pos)

    return None, None