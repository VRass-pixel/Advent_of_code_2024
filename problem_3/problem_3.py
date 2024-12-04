import re

with open(problem_3/input_3.txt) as file:
    file_contents = file.read()

mul_statements = re.findall('/mul\(\d+,\d+\)/gm', file_contents)