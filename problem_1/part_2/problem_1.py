def calculate_similarity_score(left_list, right_list):
    # Count the frequency of each number in the right list
    frequency = {}
    for number in right_list:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
            
    # Calculate the similarity score
    similarity_score = 0
    for number in left_list:
        count_in_right = frequency.get(number, 0)  # Get the count or 0 if not found
        similarity_score += number * count_in_right
        
    return similarity_score

def read_lists_from_file(filename):
    left_list = []
    right_list = []
    
    with open(filename, 'r') as file:
        for line in file:
            numbers = line.split()  # Split by whitespace
            if len(numbers) == 2:     # Ensure there are exactly two numbers
                left_list.append(int(numbers[0]))
                right_list.append(int(numbers[1]))
    
    return left_list, right_list

# File input
filename = 'problem_1/input.txt'  # Change this to your actual file path
left_list, right_list = read_lists_from_file(filename)

# Calculate the similarity score
score = calculate_similarity_score(left_list, right_list)
print(f'The similarity score is: {score}')