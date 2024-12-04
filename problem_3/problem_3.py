import re

with open int('problem_3/input_3.txt', 'r') as file:
    file_contents = file.read()
    mul_statements = re.findall('mul\((\d+),(\d+)\)', file_contents)
    mul_free = [(x * y) for x, y in file]