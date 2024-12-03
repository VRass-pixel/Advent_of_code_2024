def is_report_safe(report):
    # Check the differences between consecutive levels
    for i in range(1, len(report)):
        difference = report[i] - report[i - 1]
        # Unsafe conditions
        if difference > 2 or difference < -2 or difference == 0:
            return False
    return True


def calculate_safe_reports(column_lists):
    safe_count = 0
    
    # Check each report
    for report in column_lists:
        if is_report_safe(report):
            safe_count += 1
            print(f"Report {report} is Safe")
        else:
            print(f"Report {report} is Unsafe")
    
    return safe_count

# Read file + split definition
def read_file_and_split(filename):
    column_lists = []
    
    with open(filename, 'r') as file:
        for line in file:
            # Split into numbers, convert to integers, and store in column_lists
            numbers = list(map(int, line.split()))
            column_lists.append(numbers)  # Append the entire report as a list

    return column_lists

# File name input here
filename = 'problem_2/input-1.txt'  # Specify the input file path here

# Read + split call
column_lists = read_file_and_split(filename)

# Total safe reports
total_safe_reports = calculate_safe_reports(column_lists)

print(f"Total Safe Reports: {total_safe_reports}")