def is_report_safe(report):
    if len(report) < 2:
        return True  # A report with less than 2 levels is trivially safe

    # Check initial differences direction
    is_increasing = report[1] > report[0]
    
    for i in range(1, len(report)):
        difference = report[i] - report[i - 1]
        
        # Check if the difference is within 1 to 3
        if difference < 1 or difference > 3:
            return False
        
        # Check if the trend (increasing/decreasing) is consistent
        current_increasing = report[i] > report[i - 1]
        if current_increasing != is_increasing:
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