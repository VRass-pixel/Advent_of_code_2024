def calculate_distance(column_lists):
    # Check if all columns are of the same length
    length = len(column_lists[0])

    # List sorter
    sorted_columns = [sorted(column) for column in column_lists]

    # Distance measure starts here!!!
    total_distances = [0] * (len(sorted_columns) - 1)

    # Calculate distances for each pair
    for i in range(length):  # iterate through rows
        for j in range(1, len(sorted_columns)):  # compare with all other columns
            distance = abs(sorted_columns[0][i] - sorted_columns[j][i])
            total_distances[j - 1] += distance
            # Dialogue for check
            print(f"Pairing: ({sorted_columns[0][i]}, {sorted_columns[j][i]}) -> Distance: {distance}")

    return total_distances

# Read file + split definition
def read_file_and_split(filename):
    column_lists = []
    
    with open(filename, 'r') as file:
        for line in file:
            # Split into numbers, convert to integers, and store in column_lists
            numbers = list(map(int, line.split()))
            # Extend the column lists to accommodate new entries
            if not column_lists:
                column_lists = [[] for _ in range(len(numbers))]
            for idx, number in enumerate(numbers):
                column_lists[idx].append(number)

    return column_lists

# File name input here!!!
filename = 'input-1.txt'  # this is where you input stuff REMEMBER future Vitaly!!!!!!

# Read + split call!!!
column_lists = read_file_and_split(filename)

# Total distance
total_distances = calculate_distance(column_lists)