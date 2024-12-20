import re

with open ('problem_3/input_3.txt', 'r') as file:
    file_contents = file.read()
    mul_statements = re.findall('mul\((\d+),(\d+)\)', file_contents)
    mul_results = [int(x) * int(y) for x, y in mul_statements]
    total_sum = sum(mul_results)
    print(f"Total sum of multiplication results: {total_sum}")