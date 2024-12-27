def parse_schematic(schematic):
    # Parse the schematic into a list of heights
    # A height is the count of `#` characters in a column
    heights = []
    rows = schematic.strip().split('\n')
    num_columns = len(rows[0])  # Number of columns (locks or keys)
    
    # Process each column
    for col in range(num_columns):
        height = sum(1 for row in rows if row[col] == '#')
        heights.append(height)
    
    return heights

def fits(lock_heights, key_heights):
    # Check if a given lock and key pair fit without overlapping
    for lock_height, key_height in zip(lock_heights, key_heights):
        if lock_height + key_height > len(lock_heights):
            return False
    return True

def count_fitting_pairs(locks, keys):
    count = 0
    for lock in locks:
        lock_heights = parse_schematic(lock)
        for key in keys:
            key_heights = parse_schematic(key)
            if fits(lock_heights, key_heights):
                count += 1
    return count

def read_input_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read().strip().split("\n\n")
        
        # Separate locks and keys (assuming first part is locks, second part is keys)
        locks = content[0].strip().split("\n")
        keys = content[1].strip().split("\n")
        
        return locks, keys

locks, keys = read_input_from_file('problem_25/input_25.txt')

# Output the number of fitting pairs
print(count_fitting_pairs(locks, keys))
