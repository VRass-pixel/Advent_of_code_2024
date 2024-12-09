def find_word(wordsearch, word):
    """Tries to find word in wordsearch and prints the count of occurrences"""
    start_pos = []
    first_char = word[0]
    
    # Store all starting positions where the first character matches
    for i in range(len(wordsearch)):
        for j in range(len(wordsearch[i])):
            if wordsearch[i][j] == first_char:
                start_pos.append([i, j])
    
    word_count = 0
    
    # Check all starting positions for the word
    for p in start_pos:
        word_count += check_start(wordsearch, word, p)
    
    if word_count > 0:
        print(f'Word "{word}" found {word_count} times.')
    else:
        print('Word not found')


def check_start(wordsearch, word, start_pos):
    """Checks if the word starts at the startPos. Returns the number of times the word is found"""
    directions = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
    word_count = 0
    
    # Try each direction and count the valid occurrences of the word
    for d in directions:
        if check_dir(wordsearch, word, start_pos, d):
            word_count += 1
    
    return word_count


def check_dir(wordsearch, word, start_pos, dir):
    """Checks if the word is found in a given direction from start_pos. Returns True if found"""
    found_chars = [word[0]]  # Start with the first character
    current_pos = start_pos  # Current position in wordsearch
    pos = [start_pos]  # Positions of the found word characters
    
    # Check if the word matches in the given direction
    while chars_match(found_chars, word):
        if len(found_chars) == len(word):
            return True  # Word is fully found in this direction
        
        # Move to the next character in the given direction
        current_pos = [current_pos[0] + dir[0], current_pos[1] + dir[1]]
        pos.append(current_pos)
        
        if is_valid_index(wordsearch, current_pos[0], current_pos[1]):
            found_chars.append(wordsearch[current_pos[0]][current_pos[1]])
        else:
            return False  # Out of bounds
    
    return False


def chars_match(found, word):
    """Checks if the letters found match the start of the word we are looking for"""
    return found == list(word[:len(found)])


def is_valid_index(wordsearch, line_num, col_num):
    """Checks if the provided line number and column number are valid"""
    return 0 <= line_num < len(wordsearch) and 0 <= col_num < len(wordsearch[line_num])


##########################################################################################################
# Program Starts Here
##########################################################################################################

# import wordsearch
print('')
with open('problem_4/input_4.txt', 'r') as file:
    wordsearch = file.read().splitlines()

# Ask for word to look for
while True:
    word = 'XMAS'  # Example word
    find_word(wordsearch, word)
