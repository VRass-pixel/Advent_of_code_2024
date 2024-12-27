def read_variables(file_path):
    variables = {}
    equations = []
    
    with open(file_path, 'r') as file:
        for line in file:
            # Read variable values
            if ':' in line:
                var, value = line.split(':')
                variables[var.strip()] = int(value.strip())
            else:
                # Read equations
                equations.append(line.strip())
    
    return variables, equations

def evaluate_expression(expr, variables):
    # Replace XOR, OR, AND with respective operations
    expr = expr.replace("XOR", "^").replace("OR", "|").replace("AND", "&")
    try:
        # Use eval() to evaluate the expression
        return eval(expr, {}, variables)
    except Exception as e:
        print(f"Error evaluating expression '{expr}': {e}")
        return None

def solve_equations(variables, equations):
    results = {}
    failed_equations = []
    
    # First pass: Evaluate all equations
    for equation in equations:
        if '->' in equation:
            left, right = equation.split('->')
            left = left.strip()
            right = right.strip()
            
            result = evaluate_expression(left, variables)
            if result is not None:
                results[right] = result
                # Store result in variables for future equations
                variables[right] = result
            else:
                failed_equations.append(equation)  # Track failed equations
    
    return results, failed_equations

def retry_failed_equations(variables, failed_equations):
    results = {}
    newer_failed_equations = []
    
    for equation in failed_equations:
        if '->' in equation:
            left, right = equation.split('->')
            left = left.strip()
            right = right.strip()
            
            result = evaluate_expression(left, variables)
            if result is not None:
                results[right] = result
                variables[right] = result  # Update the variable with the new result
            else:
                newer_failed_equations.append(equation)  # Still failed
    
    return results, newer_failed_equations

def main():
    file_path = 'problem_24/input_24.txt'  # Change this to your actual file path
    variables, equations = read_variables(file_path)
    
    print("Initial Variables:", variables)
    print("Equations to solve:", equations)
    
    # First attempt to solve equations
    results, failed_equations = solve_equations(variables, equations)

    # Print initial results
    if results:
        print("\nResults after first pass:")
        for var, value in results.items():
            print(f"{var}: {value}")
    
    # Retry logic for failed equations
    while failed_equations:
        print("\nRetrying failed equations...")
        new_results, failed_equations = retry_failed_equations(variables, failed_equations)

        if new_results:
            for var, value in new_results.items():
                print(f"{var}: {value}")

        # Update the variable dictionary with new results
        variables.update(new_results)

    if not failed_equations:
        print("\nAll equations evaluated successfully!")

    # Print all solved variables at the end
    print("\nAll Solved Variables:")
    for var, value in variables.items():
        print(f"{var}: {value}")  # Print all variables and their values

    # Collecting all solved variables starting with 'z'
    z_variables = {var: value for var, value in variables.items() if var.startswith('z')}

    # Sorting the z variables by variable name in descending order
    sorted_z_vars = sorted(z_variables.keys(), reverse=True)

    # Constructing the binary number from highest to lowest
    binary_number = ''.join(str(z_variables[var]) for var in sorted_z_vars)

    # Print the constructed binary number
    print("\nCombined Binary Number from z variables:", binary_number)
    binary_input = binary_number
    decimal_output = int(binary_input, 2)
    print(f"decimal_output = {decimal_output}")

if __name__ == '__main__':
    main()
