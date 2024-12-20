def simulate_guard_path(map_input):
    # Direction vectors for Up, Right, Down, Left
    direction_map = {
        '^': (-1, 0),  # Up
        '>': (0, 1),   # Right
        'v': (1, 0),   # Down
        '<': (0, -1)   # Left
    }
    
    # Convert the input map into a 2D list of characters (grid)
    grid = [list(line) for line in map_input.strip().split('\n')]
    
    # Find the initial position of the guard and the initial direction
    start_row, start_col, start_dir = None, None, None
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] in direction_map:
                start_row, start_col, start_dir = row, col, grid[row][col]
                break
        if start_row is not None:
            break
    
    # Set of visited positions
    visited = set()
    row, col, direction = start_row, start_col, start_dir
    
    # Track the initial position as visited
    visited.add((row, col))
    
    # Simulate the movement of the guard
    while True:
        # Get the next position based on the current direction
        d_row, d_col = direction_map[direction]
        next_row, next_col = row + d_row, col + d_col
        
        # Check if the next position is out of bounds
        if not (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])):
            break
        
        # Check if the next position is an obstacle
        if grid[next_row][next_col] == '#':
            # Turn right 90 degrees
            direction = {'^': '>', '>': 'v', 'v': '<', '<': '^'}[direction]
        else:
            # Move to the next position
            row, col = next_row, next_col
            visited.add((row, col))
    
    # Return the number of distinct visited positions
    return len(visited)

# Example Input
map_input = """
..........................#.#........................................#..........................................#.............#...
....................#...............................#.......#...............................#..........................#...#......
.....#.......#...................................................#..#....................##.........#...#...........#.....#..#.#..
............#...#....#..............##...#.#....#........................#...................................................#....
....#......##........................................................................#..#..##...................##.........#......
.............##.........#..##..............#...............#....................#..................#......#...................#...
...........#.....................#.......#.................#....#.#..............#...........#.........................#..........
.#............#..............................................................#........#................#........#.................
..........................#..#.......................................................#.........#..................................
.........#....#................#...........#...................##............#..........#.........................................
....#...................................#....#.........#..........#.......................#..............................#........
.............................#.....##.............................................................#..#...........................#
....#................#...#.#..........#.#....#..................#..........#......#.............................#.................
......................#............#......................................##................#..........#..#.............#.........
..#........#............#.....###....##...........................#..............................#.....#..........................
.....#...........#..#.........#...................#.#.................#........#............#.....#........#......................
..........................................................................................................................#.......
..#...................#.....................................................................#....................#................
...............#............................#....#..........#...................#............#...............#..#.................
................#...........................#...........................................#.........................#...............
..........#.......#.........................##.................................................#...................##..#..........
.#.........#...#..#............................................#........................#.......................................#.
........#...........###..................#...........#..............#.....................#................#......................
.............#....#............................#.#..............................#..#................................#.............
...#.....#..........#...........#..................................................#........#...........#..#..........##.....#....
...............................................................................#...................#........................##....
......#.#...........................#.................#.................................................................#.........
..................................#............................................................................#.#................
........................#.......#.....#..........#..#.............##.................#..............#............##...............
......#........................#........................................#......#..................................................
...............##.......#..............................................................................................#..........
....#...................................................................................#.........#..........#..............#.....
.....#.............#.........................#.........#........#................#.#.........................#..........#.........
.............#......##...........#................#...#.#.....#......................................#..........#.................
...........................#............#................#................#...........................#.....#.....................
.......#.................#..#..............#................................#....#........#.......#.............#....#....##......
........................................................#........................................................................#
.................#.........................................#.......#.......#......#...#.#.................##......................
..........#............#..............................................#........................................#..........#..#....
..............#......................................................#......#................................#....................
...#........#.............#.................#......#.......................#..............................##........#.............
.....................#............................................................#............#...............................#..
......#.....#..............................................................#...............#...#..................................
.......................................#..#.......#...#..............#.................................................#..........
...................................................................................................#........................#.....
....#.....#.......................................................#.....#......#...................#............#.................
..............#....#.....................#........................................##....#...#.....................................
.....#...............................................................#............#............................#..................
........................#..........................#..............................................................................
#..............#...........................................................................#......................................
...................................#...#....................................................................#.....................
................#......#.........#.................#...........................#..................................................
......#...#................#...............#..................................................#...................................
.......................#.............#..#....................#............#.......................................................
.....................#.#.....................................#................................##.............#.#..#..............#
.....................................#...#...........................#....................................................##...#..
.................#..#............#.............................#..#................................................##.............
...#...........................................#.................................................#.............#.............##...
..................#....#....#.#..........................#.............#................#............................#............
.........................#................#.#..#.#............^.........................................................#.........
.....#...............#............................................................................................................
.#.......................................................................................#...............#....#.............#.....
......#................................#............#............................................................#................
.#.....................#..............#.............#.......................#.....#....#.#.#...................#....#.............
..................................................................#........#............................#..#.#...............#....
.#.....................#......#........#.......#.................#.......................#..#.....................................
..............#..#..#.............................................#....................#......#...................................
.................##.#............................##..#...............................................................#....#.......
...........#..#........................#.#..........#.................##.....#...#.........................#.#...#............#...
.....................#..........#..#..............................................................................................
.......#...............................#..#.........#.....................................#......#...................#............
..............................##.#........#.......#..#.....#......................................................................
..................#......................#.....................................###...#............................##..............
...................................#...................................#...........................#....##..#.....................
.....................#.....#.#.........#.........................#.....#.......#..........#.......................#...............
...........#..................................................................................................#...................
......#............................#.............................#..........................................#.....##..............
...........................#...........................................................#.............................#..........#.
..........................................#..........................................#......#...............#.....................
..............##.........#........................................................................................................
.....................#............#..#......#..#......................................................................#...........
........#.........#.....................#.................................#...#.#....#....#......................#.#..............
......#...........#............................................................#..............#......................#............
.....#.....................#.....#.........#.............................#....#............................#......................
..#..............................................................................................................#...#............
..............#.......................#........#............................................#.......................#.............
........................................#....................................................................................##...
.......#..#.......#.................#.#.................#...........#............#........#.#.........#...........#.#..........#..
.....##.......................#.........................#.........................#...........#.........#.....#...........#.......
..........................#.....................#...............................#.............................#...................
.....#..........#.............#...#..........................#.#...................#...........................#......#...........
......................................#.......#.........#......................................#..................................
......#...#....................#................#...#.......#.............#............#...........#.....#........................
........................................#............#......................................................#............#........
..#.......#....#..........................................................................#......................##..#.......#....
................#...................................................#..........................................#..................
...........#........................................................................................#.............................
..................#........................................#.....#...........................#..................#.................
........#.......#.....#...........#.......................................................#.........#.............................
.............#.....#.#............................#...................................................................#...........
...............#...................................#...........................#.............#..#..................#..##..........
.#...............................#....#.....................#...................................#...................#...#.........
..................#..#.#..................................................................................................#.......
.........#.....#...#.........#........#...........................................#..................#.#.#......#.................
.........#......#.......................#........#.............................#...#................#...........................#.
...#.........................................................................................##........................#..........
.....................................#...........................................................#.#...#......#...............#...
#.....................#.........#.................................................#.....................................#.........
............##.............................#...............................................#......................................
.#.................#........................#.................................................................#.....#.............
.....#.......................#......................#.................#....#....................................................#.
.............................#..................................................................#.#...............................
........#.......#.....##..........................................#...................#.........#...........#...#...#...#.........
..........#.#...#.....................#............................................................##.........##..................
...................#..............##.....#...........#.#.......#................................................#...............#.
............................................................#....#.............#....##.......#...#...#................#...........
......#...............................#.........#...................#....#..............#.................#.......................
....................................#.....................#....#....#.................#...............#...........................
.................................#.............#.#...................................#..............#...#.....#.............#.....
......................#..................#.............#.................#................................................#.......
.....................##.......................#.............#...#........#..........#.....#............................##...#.....
..........................#.....................#...........#.....................................................#...............
................#.....................................................................................................#...........
........#......#.......................#....................................#................................#....................
.....................................#............................................................................................
........#..........#.........#.#................##................#...#..........................#.........#......##.......#......
.......#...................#................................#..#.......................#..............................#...........
............#.....................................#......#........................#..........#.............................#......
..#...........#...........#...................................#............#...#.....#......................................#.....
................................................................#...........#.......##.......#..........#............#............
"""

# Run the simulation and print the result
result = simulate_guard_path(map_input)
print(result)