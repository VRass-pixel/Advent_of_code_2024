#x01 XOR y01 -> z01
#x02 OR y02 -> z02

#####
########################
#UPDATE THIS FROM THE ACTUAL DOCUMENT
line_gap = 7 
########################

with open("problem_24/test.txt", 'r') as src:   #### HERE
    lines = src.readlines()

# Split the lines into two parts
part1 = lines[:line_gap]
part2 = lines[line_gap:]

# Write the first part to the first output file
with open('problem_24/file1.txt', 'w') as f1:
    f1.writelines(part1)

# Write the second part to the second output file
with open('problem_24/file2.txt', 'w') as f2:
    f2.writelines(part2)

#####################
with open('problem_24/file1.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip().replace(':', '=')

    # Execute
    exec(line)

    print(f"Executed: {line}")

print(y01 + x02)


###############
# Binary --> Decemal
###############
#binary_number = ""
#decimal_number = int(binary_number, 2)
#print (decimal_number)
###############