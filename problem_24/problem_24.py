import numpy as np

######################
# Update this from the actual document
line_gap = 11  # Adjust this based on the actual input

# Read input file
with open("problem_24/test.txt", 'r') as src:
    lines = src.readlines()

# Split the lines into two parts based on the line gap
part1 = lines[:line_gap]
part2 = lines[line_gap:]

variables = {}
for line in part1:
    line = line.strip()
    
    # Skip empty lines
    if not line:
        continue
    
    # Split the line by ':' and check if there are exactly 2 parts
    parts = line.split(':')
    
    if len(parts) != 2:
        print(f"Skipping malformed line: {line}")
        continue  # Skip malformed lines
    
    wire, value = parts
    variables[wire] = int(value)

# Parse the gates from part2
gates = []
for line in part2:
    line = line.strip()
    if not line:  # Skip empty lines
        continue
    
    # Replace logical operators with numpy equivalents
    line = line.replace('AND', 'np.bitwise_and') \
               .replace('XOR', 'np.bitwise_xor') \
               .replace('OR', 'np.bitwise_or')

    # Replace '->' with '==' for assignment
    line = line.replace('->', '==')

    # Split the line by '==' to extract LHS and RHS
    parts = line.split('==')
    
    # If the line does not contain exactly one '==', print an error or skip it
    if len(parts) != 2:
        print(f"Skipping invalid line: {line}")
        continue
    
    lhs_expr = parts[0].strip()
    rhs_var = parts[1].strip()

    # Add the valid gate equation to the gates list
    gates.append((lhs_expr, rhs_var))

######################
# Function to solve all equations iteratively using numpy
def solve_equations(gates, variables):
    solved_values = variables.copy()  # Start with initial variables
    unsolved = set([rhs_var for _, rhs_var in gates])  # Set of variables we need to solve
    processing = set()  # Set to track variables currently being processed
    iteration_count = 0  # To limit infinite retries
    progress_made = False  # Flag to track if any new variables are being solved

    while unsolved:
        iteration_count += 1
        if iteration_count > 100:
            print("Too many iterations, exiting to avoid infinite loop.")
            break

        progress = False  # Flag to track if we can make progress in this iteration
        print(f"\n--- Iteration {iteration_count} ---")
        print(f"Solved Values: {solved_values}")
        print(f"Unsolved Variables: {unsolved}")

        for lhs_expr, rhs_var in gates:
            if rhs_var in solved_values:
                continue  # Skip already solved variables

            lhs_vars = lhs_expr.split()  # Split LHS into individual variables

            # Check if all variables in lhs_expr are known
            if all(var in solved_values for var in lhs_vars):
                if rhs_var in processing:
                    # Circular dependency detected
                    print(f"Circular dependency detected while processing {rhs_var}. Skipping.")
                    continue  # Skip this equation for now and retry later
                
                try:
                    # Add the current rhs_var to processing set (mark as being processed)
                    processing.add(rhs_var)
                    
                    # Evaluate the expression on the left-hand side (LHS)
                    lhs_result = eval(lhs_expr, {}, solved_values)  # Use current known values

                    # Store the result and mark as solved
                    solved_values[rhs_var] = lhs_result
                    unsolved.remove(rhs_var)
                    processing.remove(rhs_var)  # Done processing, remove from the set
                    progress = True  # Progress made in solving the equations

                    # Track progress
                    progress_made = True
                    print(f"Assigned: {rhs_var} = {lhs_result}")

                except Exception as e:
                    print(f"Error evaluating {lhs_expr}: {e}")

        # If no progress was made, retry in the next iteration
        if not progress:
            if progress_made:
                print("Progress made in this iteration, retrying with updated known values.")
            else:
                print("Unable to make progress, retrying with current known values.")
            # Implementing a delay would help mitigate infinite retries
            import time
            time.sleep(1)  # Wait 1 second before retrying (can adjust this delay)

    return solved_values

# Solve all the equations
final_values = solve_equations(gates, variables)

# Print out the final solved values
print("\nFinal solved values:")
for var, value in final_values.items():
    print(f"{var} = {value}")

# Binary --> Decimal Conversion
# After solving the equations, we will now convert the binary results (e.g., z variables) into decimal numbers.
binary_number = "".join(str(final_values.get(f'z{i:02}', 0)) for i in range(13))  # Assuming 13 z variables
decimal_number = int(binary_number, 2)

print(f"Binary Number: {binary_number}")
print(f"Decimal Number: {decimal_number}")
