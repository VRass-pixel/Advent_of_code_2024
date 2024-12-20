import re

def process_input(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
        
        multiplication_enabled = True  # Start with multiplication enabled
        total_sum = 0  # Initialize total sum of results
        
        # Split the input using regex to handle various characters
        tokens = re.split(r'([()])|[\s]', file_contents)  # Split around () and spaces

        # Filter out None values and empty strings from tokens
        tokens = [t for t in tokens if t and t.strip()]

        for token in tokens:
            token = token.strip()  # Clean up white spaces
            
            if token == "do()":
                multiplication_enabled = True  # Enable multiplication
            elif token == "don't()":
                multiplication_enabled = False  # Disable multiplication
            elif token.startswith("mul(") and multiplication_enabled:
                # Extract numbers from the mul function
                match = re.match(r'mul\((\d+),(\d+)\)', token)
                if match:
                    x, y = map(int, match.groups())
                    total_sum += x * y  # Calculate and add to total sum

        return total_sum

# Call the function and print the result
result = process_input('problem_3/input_3.txt')
print(f"Total sum of multiplication results: {result}")