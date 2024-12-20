def calculate_distance(left_list, right_list):
    # list sorter
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    # list sorter job check
    if len(left_sorted) != len(right_sorted):
        print("The lists must be of the same length.")
        return None

    # distance mesurer starts here!!!
    total_distance = 0
    # paring + take away function distance resuly
    for i in range(len(left_sorted)):
        distance = abs(left_sorted[i] - right_sorted[i])
        total_distance += distance
        # dialogue for check
        print(f"Pairing: ({left_sorted[i]}, {right_sorted[i]}) -> Distance: {distance}")

    return total_distance

# read file + split definition
def read_file_and_split(filename):
    left_list = []
    right_list = []
    
    with open(filename, 'r') as file:
        for line in file:
            # split to 2 numbers + add to dict
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    return left_list, right_list

# file name input here!!!
filename = 'problem_1/input.txt'  # this is where you input stuff REMEMBER future Vitaly!!!!!!

# Read + split call!!!
left_list, right_list = read_file_and_split(filename)

# total distance
total_distance = calculate_distance(left_list, right_list)

# Answer is printed:
if total_distance is not None:
    print(f"Total distance between paired numbers: {total_distance}")