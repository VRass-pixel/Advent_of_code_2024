from collections import defaultdict

# Step 1: Parse the input
def parse_input(ordering_rules, updates):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Create the graph from the ordering rules
    for rule in ordering_rules:
        before, after = map(int, rule.split('|'))
        graph[before].append(after)
        in_degree[after] += 1
        if before not in in_degree:
            in_degree[before] = 0

    # Parse the updates
    updates = [list(map(int, update.split(','))) for update in updates]

    return graph, in_degree, updates

# Step 2: Check if an update is correctly ordered
def is_ordered(update, graph, in_degree):
    # We need to check the topological order of the update using Kahn's Algorithm
    # to see if it respects the ordering constraints.
    
    # Create a set of nodes with no incoming edges (in-degree 0)
    in_update = {page: 0 for page in update}
    for page in update:
        for neighbor in graph[page]:
            if neighbor in in_update:
                in_update[neighbor] += 1
    
    # Apply Kahn's algorithm to check for topological order
    queue = [page for page in in_update if in_update[page] == 0]
    
    ordered_pages = []
    while queue:
        page = queue.pop(0)
        ordered_pages.append(page)
        
        # Check if all neighbors are now ready to be added to the queue
        for neighbor in graph[page]:
            if neighbor in in_update:
                in_update[neighbor] -= 1
                if in_update[neighbor] == 0:
                    queue.append(neighbor)
    
    # If the ordered pages match the update, it's correct
    return ordered_pages == update

# Step 3: Find the middle page of a correctly ordered update
def find_middle(update):
    mid_index = len(update) // 2
    return update[mid_index]

# Step 4: Solve the problem
def solve(ordering_rules, updates):
    graph, in_degree, updates = parse_input(ordering_rules, updates)
    
    total = 0
    for update in updates:
        if is_ordered(update, graph, in_degree):
            total += find_middle(update)
    
    return total

# Example usage
ordering_rules = [
"88|12", "44|33", "44|26", "29|91", "29|23", "29|84", "19|17", "19|84", "19|53", "19|79", "23|48", "23|31", "23|12", "23|72", "23|98", "18|44", "18|88", "18|94", "18|41", "18|83", "18|31", "26|48", "26|43", "26|86", "26|87", "26|15", "26|24", "26|27", "86|55", "86|91", "86|74", "86|98", "86|13", "86|48", "86|36", "86|67", "13|43", "13|49", "13|53", "13|94", "13|88", "13|24", "13|19", "13|16", "13|72", "42|21", "42|23", "42|75", "42|67", "42|54", "42|36", "42|62", "42|58", "42|84", "42|29", "72|53", "72|16", "72|17", "72|79", "72|52", "72|38", "72|29", "72|94", "72|45", "72|83", "72|19", "94|61", "94|35", "94|12", "94|16", "94|75", "94|31", "94|17", "94|78", "94|44", "94|29", "94|33", "94|52", "58|67", "58|37", "58|18", "58|49", "58|72", "58|23", "58|13", "58|74", "58|43", "58|95", "58|91", "58|48", "58|55", "67|52", "67|55", "67|27", "67|33", "67|94", "67|43", "67|23", "67|31", "67|41", "67|19", "67|72", "67|45", "67|18", "67|21", "35|55", "35|37", "35|95", "35|74", "35|87", "35|21", "35|89", "35|86", "35|43", "35|26", "35|67", "35|15", "35|13", "35|58", "35|18", "98|78", "98|75", "98|17", "98|94", "98|44", "98|62", "98|12", "98|33", "98|61", "98|29", "98|79", "98|42", "98|38", "98|53", "98|31", "98|45", "84|49", "84|13", "84|72", "84|67", "84|48", "84|23", "84|89", "84|94", "84|24", "84|15", "84|95", "84|91", "84|74", "84|86", "84|55", "84|27", "84|21", "53|58", "53|86", "53|35", "53|91", "53|17", "53|79", "53|16", "53|87", "53|37", "53|62", "53|36", "53|15", "53|12", "53|78", "53|26", "53|67", "53|75", "53|89", "79|95", "79|86", "79|89", "79|58", "79|27", "79|67", "79|18", "79|36", "79|87", "79|26", "79|84", "79|43", "79|35", "79|21", "79|23", "79|13", "79|48", "79|74", "79|49", "55|31", "55|18", "55|42", "55|45", "55|49", "55|72", "55|24", "55|12", "55|98", "55|41", "55|13", "55|44", "55|94", "55|52", "55|43", "55|17", "55|38", "55|61", "55|19", "55|88", "38|26", "38|29", "38|84", "38|42", "38|54", "38|79", "38|53", "38|52", "38|75", "38|33", "38|17", "38|45", "38|41", "38|88", "38|19", "38|58", "38|61", "38|83", "38|78", "38|62", "38|16", "24|38", "24|16", "24|78", "24|83", "24|98", "24|88", "24|19", "24|12", "24|53", "24|44", "24|94", "24|62", "24|35", "24|41", "24|52", "24|79", "24|54", "24|33", "24|29", "24|31", "24|45", "24|17", "21|13", "21|18", "21|41", "21|45", "21|53", "21|38", "21|55", "21|94", "21|24", "21|48", "21|98", "21|43", "21|49", "21|19", "21|52", "21|61", "21|23", "21|88", "21|44", "21|31", "21|83", "21|33", "21|72", "15|88", "15|41", "15|55", "15|18", "15|89", "15|23", "15|48", "15|31", "15|72", "15|43", "15|44", "15|27", "15|21", "15|38", "15|19", "15|98", "15|13", "15|74", "15|94", "15|52", "15|49", "15|83", "15|24", "15|67", "33|16", "33|89", "33|54", "33|84", "33|91", "33|53", "33|86", "33|26", "33|75", "33|37", "33|12", "33|74", "33|58", "33|87", "33|35", "33|36", "33|15", "33|95", "33|17", "33|29", "33|78", "33|79", "33|62", "33|42", "74|49", "74|83", "74|31", "74|72", "74|98", "74|67", "74|52", "74|61", "74|43", "74|94", "74|24", "74|18", "74|19", "74|23", "74|55", "74|13", "74|27", "74|44", "74|88", "74|21", "74|45", "74|38", "74|48", "74|41", "36|15", "36|94", "36|44", "36|24", "36|48", "36|21", "36|18", "36|13", "36|55", "36|49", "36|98", "36|27", "36|41", "36|38", "36|23", "36|67", "36|95", "36|89", "36|88", "36|43", "36|31", "36|72", "36|52", "36|74", "27|52", "27|94", "27|61", "27|38", "27|41", "27|24", "27|18", "27|19", "27|44", "27|49", "27|43", "27|33", "27|83", "27|45", "27|12", "27|16", "27|48", "27|13", "27|72", "27|98", "27|53", "27|55", "27|88", "27|31", "87|21", "87|27", "87|94", "87|48", "87|43", "87|49", "87|58", "87|67", "87|13", "87|72", "87|15", "87|36", "87|91", "87|24", "87|86", "87|18", "87|95", "87|37", "87|55", "87|89", "87|44", "87|98", "87|74", "87|23", "45|16", "45|36", "45|75", "45|62", "45|95", "45|54", "45|35", "45|84", "45|87", "45|86", "45|58", "45|79", "45|17", "45|12", "45|29", "45|15", "45|33", "45|26", "45|53", "45|37", "45|61", "45|78", "45|91", "45|42", "43|62", "43|16", "43|45", "43|94", "43|41", "43|98", "43|53", "43|61", "43|52", "43|24", "43|54", "43|19", "43|17", "43|78", "43|33", "43|42", "43|29", "43|88", "43|12", "43|38", "43|72", "43|83", "43|44", "43|31", "37|95", "37|48", "37|43", "37|41", "37|23", "37|67", "37|31", "37|55", "37|13", "37|74", "37|98", "37|18", "37|36", "37|44", "37|38", "37|89", "37|15", "37|49", "37|21", "37|24", "37|27", "37|72", "37|94", "37|91", "49|94", "49|83", "49|24", "49|16", "49|72", "49|61", "49|44", "49|17", "49|41", "49|54", "49|78", "49|98", "49|62", "49|42", "49|19", "49|33", "49|12", "49|38", "49|53", "49|45", "49|31", "49|88", "49|43", "49|52", "52|88", "52|16", "52|33", "52|26", "52|42", "52|17", "52|35", "52|62", "52|84", "52|54", "52|87", "52|37", "52|19", "52|75", "52|83", "52|53", "52|12", "52|78", "52|86", "52|45", "52|61", "52|58", "52|79", "52|29", "16|67", "16|23", "16|42", "16|91", "16|17", "16|79", "16|37", "16|95", "16|29", "16|89", "16|36", "16|62", "16|26", "16|87", "16|78", "16|75", "16|21", "16|15", "16|35", "16|86", "16|54", "16|84", "16|74", "16|58", "83|17", "83|45", "83|79", "83|37", "83|35", "83|16", "83|91", "83|36", "83|19", "83|78", "83|54", "83|84", "83|42", "83|75", "83|29", "83|26", "83|87", "83|33", "83|61", "83|62", "83|86", "83|53", "83|58", "83|12", "62|29", "62|58", "62|21", "62|74", "62|35", "62|55", "62|79", "62|23", "62|27", "62|86", "62|95", "62|36", "62|26", "62|84", "62|18", "62|75", "62|67", "62|89", "62|91", "62|87", "62|15", "62|48", "62|13", "62|37", "61|87", "61|79", "61|86", "61|26", "61|29", "61|12", "61|53", "61|75", "61|36", "61|84", "61|62", "61|35", "61|16", "61|37", "61|17", "61|54", "61|15", "61|58", "61|42", "61|95", "61|78", "61|91", "61|33", "61|89", "75|95", "75|74", "75|67", "75|13", "75|37", "75|49", "75|58", "75|87", "75|23", "75|89", "75|26", "75|27", "75|15", "75|21", "75|72", "75|55", "75|48", "75|84", "75|91", "75|18", "75|43", "75|24", "75|36", "75|86", "48|52", "48|83", "48|45", "48|31", "48|44", "48|53", "48|88", "48|98", "48|61", "48|55", "48|43", "48|33", "48|18", "48|72", "48|16", "48|13", "48|42", "48|24", "48|41", "48|94", "48|38", "48|19", "48|12", "48|49", "17|62", "17|91", "17|75", "17|37", "17|26", "17|35", "17|29", "17|23", "17|84", "17|36", "17|58", "17|15", "17|78", "17|67", "17|48", "17|89", "17|54", "17|95", "17|86", "17|79", "17|27", "17|74", "17|21", "17|87", "31|88", "31|29", "31|16", "31|45", "31|75", "31|79", "31|84", "31|87", "31|78", "31|38", "31|19", "31|52", "31|35", "31|26", "31|61", "31|41", "31|33", "31|53", "31|42", "31|17", "31|83", "31|62", "31|54", "31|12", "78|84", "78|74", "78|48", "78|89", "78|55", "78|29", "78|62", "78|37", "78|54", "78|87", "78|67", "78|79", "78|91", "78|35", "78|26", "78|36", "78|58", "78|15", "78|27", "78|95", "78|75", "78|21", "78|86", "78|23", "12|86", "12|15", "12|21", "12|58", "12|67", "12|89", "12|95", "12|26", "12|75", "12|36", "12|37", "12|29", "12|84", "12|91", "12|74", "12|35", "12|42", "12|62", "12|79", "12|54", "12|17", "12|78", "12|87", "12|16", "41|45", "41|52", "41|78", "41|42", "41|88", "41|87", "41|26", "41|35", "41|58", "41|29", "41|75", "41|84", "41|17", "41|86", "41|54", "41|33", "41|53", "41|79", "41|61", "41|16", "41|19", "41|83", "41|12", "41|62", "54|67", "54|26", "54|27", "54|86", "54|75", "54|89", "54|79", "54|23", "54|48", "54|29", "54|37", "54|18", "54|62", "54|95", "54|58", "54|36", "54|21", "54|87", "54|84", "54|35", "54|74", "54|15", "54|91", "54|55", "91|41", "91|23", "91|67", "91|36", "91|24", "91|27", "91|38", "91|55", "91|98", "91|49", "91|18", "91|13", "91|72", "91|43", "91|44", "91|31", "91|48", "91|21", "91|15", "91|95", "91|74", "91|52", "91|94", "91|89", "89|98", "89|23", "89|49", "89|38", "89|31", "89|72", "89|74", "89|55", "89|43", "89|67", "89|45", "89|88", "89|83", "89|41", "89|48", "89|27", "89|52", "89|13", "89|24", "89|44", "89|94", "89|18", "89|19", "89|21", "95|67", "95|94", "95|44", "95|83", "95|88", "95|27", "95|23", "95|43", "95|89", "95|48", "95|72", "95|24", "95|55", "95|18", "95|74", "95|13", "95|21", "95|38", "95|41", "95|52", "95|15", "95|98", "95|31", "95|49", "88|84", "88|29", "88|33", "88|35", "88|78", "88|19", "88|86", "88|16", "88|37", "88|53", "88|83", "88|75", "88|45", "88|91", "88|42", "88|79", "88|54", "88|62", "88|26", "88|87", "88|17", "88|61", "88|58", "44|35", "44|42", "44|17", "44|16", "44|29", "44|83", "44|41", "44|54", "44|88", "44|62", "44|31", "44|84", "44|19", "44|75", "44|78", "44|45", "44|38", "44|12", "44|52", "44|61", "44|53", "44|79", "29|75", "29|58", "29|89", "29|13", "29|35", "29|15", "29|26", "29|95", "29|86", "29|74", "29|21", "29|55", "29|67", "29|37", "29|79", "29|87", "29|49", "29|48", "29|36", "29|27", "29|18", "19|61", "19|35", "19|33", "19|12", "19|45", "19|42", "19|95", "19|86", "19|16", "19|37", "19|26", "19|36", "19|91", "19|58", "19|54", "19|87", "19|78", "19|62", "19|29", "19|75", "23|44", "23|19", "23|43", "23|38", "23|83", "23|13", "23|61", "23|18", "23|24", "23|27", "23|49", "23|55", "23|45", "23|52", "23|53", "23|88", "23|94", "23|33", "23|41", "18|24", "18|33", "18|53", "18|19", "18|13", "18|43", "18|12", "18|78", "18|72", "18|52", "18|61", "18|45", "18|42", "18|98", "18|17", "18|49", "18|38", "18|16", "26|89", "26|49", "26|98", "26|55", "26|74", "26|13", "26|21", "26|91", "26|67", "26|36", "26|84", "26|23", "26|37", "26|58", "26|72", "26|18", "26|95", "86|94", "86|18", "86|43", "86|89", "86|37", "86|49", "86|23", "86|21", "86|72", "86|38", "86|31", "86|27", "86|15", "86|24", "86|44", "86|95", "13|83", "13|41", "13|52", "13|61", "13|44", "13|98", "13|78", "13|33", "13|17", "13|12", "13|31", "13|38", "13|42", "13|45", "13|54", "42|27", "42|35", "42|17", "42|37", "42|15", "42|91", "42|78", "42|89", "42|87", "42|86", "42|95", "42|26", "42|74", "42|79", "72|62", "72|98", "72|33", "72|24", "72|12", "72|31", "72|78", "72|44", "72|54", "72|41", "72|88", "72|42", "72|61", "94|42", "94|79", "94|26", "94|54", "94|62", "94|38", "94|83", "94|19", "94|45", "94|53", "94|41", "94|88", "58|21", "58|94", "58|36", "58|89", "58|31", "58|44", "58|98", "58|15", "58|27", "58|24", "58|86", "67|38", "67|48", "67|44", "67|61", "67|98", "67|13", "67|24", "67|49", "67|83", "67|88", "35|23", "35|91", "35|48", "35|49", "35|27", "35|75", "35|84", "35|72", "35|36", "98|35", "98|52", "98|88", "98|19", "98|41", "98|16", "98|83", "98|54", "84|58", "84|43", "84|36", "84|37", "84|18", "84|87", "84|98", "53|29", "53|54", "53|84", "53|42", "53|74", "53|95", "79|75", "79|37", "79|15", "79|55", "79|91", "55|16", "55|53", "55|83", "55|33", "38|87", "38|12", "38|35", "24|61", "24|42", "21|27"
]

updates = [
"87,86,37,91,36,95,89,67,21,23,27,48,55,18,13,49,43,72,24,98,94",
"79,16,83,58,33,35,29,52,45,61,17,54,41,12,26",
"74,49,31,72,95,27,44,23,91,89,98,67,94,18,48",
"74,44,15,48,24,18,55,49,36,38,13,89,67,52,41,31,23,43,95,98,21",
"67,94,49,55,15,98,58,95,74,87,18,21,72",
"17,89,95,36,42,91,62,75,79,74,87,23,26,86,78,29,35,54,84,58,21",
"53,79,37,74,62,58,95,89,42,12,16,17,75,86,26,36,35",
"13,84,36,23,58,48,95,89,26,55,24,49,15,87,37,21,43",
"91,74,55,18,98,94,41",
"48,21,13,67,23,98,49,18,84",
"87,74,48,18,13,24,94",
"91,36,95,89,74,21,23,27,18,13,43,72,24,98,94,44,31,38,41",
"58,43,89,95,23,49,72",
"38,41,52,83,45,33,12,42,17,78,29,35,87",
"44,23,49,37,98,31,38,95,89,74,13,67,27",
"45,74,18,19,38,23,43,67,24,48,21,98,52,94,41,49,31,83,44,72,13",
"26,87,86,91,36,95,74,21,23,27,48,18,13,49,43,72,24",
"35,26,84,87,58,86,37,91,36,15,89,74,67,21,23,27,55,18,13,49,43",
"55,18,13,49,43,72,24,98,94,44,38,41,52,88,83,19,45,61,33,53,12,,16,42"
"91,62,79,16,42,45,26,19,36,86,53,17,54,35,37",
"13,52,45,19,16,12,72,24,78",
"83,19,45,12,62,29,79,84,37",
"44,83,33,16,42",
"27,48,55,13,49,94,31,41,52,19,61,33,53",
"45,17,31,84,42,78,19,52,26,61,83,29,88,12,62",
"98,94,44,31,41,88,83,45,61,53,12,16,42,17,54,62,29,79,35",
"13,49,43,72,94,31,41,52,88,83,19,45,61,33,12,16,78",
"54,62,29,79,35,75,26,84,87,58,37,91,36,95,15,89,74,67,21,23,27,,48,55"
"33,87,88,75,16,58,42,37,78,79,62",
"61,48,41,43,94,31,55,21,98,72,88,49,45,27,24",
"74,67,21,27,48,13,43,72,24,44,41,52,88,19,45",
"17,78,54,29,79,35,26,58,37,91,15,74,67,21,27",
"53,12,42,17,62,35,75,58,37,15,74",
"74,94,52,21,72,48,49,98,23,36,31,55,24,89,15,41,18,38,43,13,67,,95,44"
"33,45,24,88,13,12,18,48,94,55,49,72,53,41,83,52,38",
"91,15,38,94,44,98,21,48,55,24,72,27,74,49,36,23,41",
"61,33,12,17,78,62,35,75,37,36,15",
"42,61,83,12,78,33,17,26,79,84,29,87,53,58,35,41,54,45,19",
"75,26,84,87,58,37,36,95,15,89,74,67,21,23,27,48,55,13,49,43,72",
"84,62,95,91,12,54,79,36,87",
"33,79,26,19,17,45,52,75,12,53,31,88,42,78,84,62,29,16,54,61,41",
"88,83,19,45,61,33,16,42,17,78,62,79,35,26,87,86,37",
"31,41,38,23,15,83,72,27,55,98,49,13,21,48,24,94,67,74,89",
"15,74,27,18,49,72,24,31,83",
"12,16,42,17,78,54,62,29,79,35,75,26,84,58,86,37,91,36,95,15,89,,74,67"
"26,19,37,42,78,35,45,16,87,54,84,53,86,83,29,33,88,58,62,79,75,,17,61"
"17,78,54,62,29,79,35,75,26,84,87,58,86,37,91,36,95,15,89,74,67,,23,27"
"18,13,49,72,24,98,44,31,38,41,52,83,45,61,33,53,17",
"18,49,43,72,98,44,88,42,17",
"83,88,53,31,18,17,41,42,49,12,98,19,44,33,94",
"61,54,31,44,42",
"26,84,58,86,37,91,95,15,74,13,24",
"26,86,37,91,36,95,55,18,13,49,24",
"86,37,91,36,23,18,13,49,43,98,31",
"16,87,45,83,78,12,17,88,54,79,75,29,84,35,19",
"72,24,44,31,38,41,52,19,61,12,16,17,78,54,62",
"75,26,84,87,86,37,91,36,95,15,89,67,21,23,18,49,43",
"48,55,43,44,88,61,16",
"78,67,87,74,36,29,75,17,95,89,15,79,58",
"61,35,86,12,33",
"94,24,27,74,87,67,48,91,18,37,36,49,23,21,55,89,15,95,13,98,86,,43,58"
"26,29,95,55,48,54,74,21,86,84,62,27,67",
"41,83,16,17,29",
"74,67,23,27,55,18,13,43,72,24,98,31,38,41,52,88,83,19,45",
"79,15,42,74,78,35,36,12,17",
"27,23,15,52,49,89,38,72,48,13,44,74,18,31,24,95,88,21,55,43,98,,41,94"
"31,55,43,72,49,12,53,88,52,44,41,27,33",
"35,75,26,84,87,58,86,37,91,36,95,15,74,67,21,23,27,48,55,18,13,,49,43"
"89,74,67,23,27,48,18,49,72,98,44,38,41,52,19",
"23,62,54,78,74",
"91,36,15,67,48,38,41",
"79,35,75,26,84,87,58,86,37,91,36,95,15,74,67,21,23,27,48,55,18,,13,49"
"86,27,55,13,49,24,98",
"38,17,41,78,19,43,12,83,54,88,49,24,98",
"79,35,75,26,84,87,58,86,37,91,95,15,89,74,67,21,23,27,48,55,18,,13,49"
"89,74,67,21,23,27,48,55,18,13,49,43,72,24,98,94,44,31,38,41,52,,88,19"
"78,16,54,62,58,26,45,33,87,84,61,19,12,37,29,36,79,53,42,17,86",
"54,29,79,35,26,84,87,58,37,91,36,95,15,89,74,67,21,23,27,48,55",
"61,36,17,45,16,33,79,54,86,37,53,91,12,29,78",
"88,19,61,12,17,78,62,29,79,35,26,58,37",
"17,78,54,62,29,35,75,26,84,87,86,37,95,15,89,23,27",
"52,24,98,17,83,31,78,33,62,53,44,88,43",
"86,36,15,27,48,98,31",
"18,55,52,24,48,13,45,38,67,61,88,41,19",
"49,52,27,23,41,48,18,43,21,98,72,74,36,13,95,67,89",
"42,37,62,16,26,89,54,91,21,58,78,79,74,87,35,86,75,84,15",
"16,17,62,29,54,75,12,79,91,53,36,78,33,86,42,84,58",
"72,24,94,44,41,52,45,61,33,16,54,62,29",
"45,61,53,12,16,42,17,78,54,29,79,75,26,84,87,37,91,36,95",
"67,19,38,43,49,89,31,88,21,48,24",
"72,21,67,23,18,55,58,49,86,98,94,15,89,87,24",
"19,79,86,83,87,12,35,52,78,62,42,88,54",
"42,78,35,75,84,87,37,21,23",
"23,91,84,37,74,75,86,67,13,89,15,21,26,87,36,27,18,48,58,95,55,,29,79"
"88,42,16,31,49,45,61,55,43",
"75,42,37,86,26,95,17,36,35,16,33,29,61,15,87,58,12,62,53,84,91",
"37,91,86,58,75,84,89,13,55,18,48,35,67,43,27,26,74,95,15",
"33,12,16,17,79,26,84,87,58,15,89",
"98,44,31,38,52,19,45,61,33,53,12,16,42,17,78,62,29,79,35",
"36,17,42,79,67,95,26,16,12,37,35",
"38,53,12,16,62,29,35,84,87",
"41,52,83,45,53,12,16,42,78,62,29,79,75,26,84,87,58",
"62,29,79,35,75,26,84,87,58,37,36,95,89,74,67,21,23,27,48,55,18",
"54,67,17,62,95,12,36,91,84,16,15,26,86,78,79,58,29,42,75,89,87",
"94,48,24,55,15,58,23,98,91,86,72,44,36,67,95,37,43,18,13,74,27,,21,89"
"18,13,49,43,44,31,38,45,61,42,17",
"95,78,29,86,15,58,42,87,37,79,17,67,26,54,74,75,12,89,84,16,62",
"35,75,26,84,87,58,86,37,91,36,95,15,89,74,67,21,27,48,55,18,49",
"37,26,58,74,48,72,75,36,84",
"12,17,33,13,42,78,53",
"44,52,62,31,79,53,24,88,45",
"13,18,31,67,72,52,27,88,45,24,74",
"86,84,17,16,29,62,87",
"83,19,45,61,33,53,12,16,42,78,54,62,29,79,35,75,26,84,87,58,86,,37,91"
"75,13,26,43,89,67,74,18,91,49,35",
"27,55,43,72,24,98,94,38,41,52,45,61,33,53,12",
"17,78,29,79,35,26,58,86,91,95,15,74,21,23,27",
"74,43,86,98,89,21,13,67,23,72,91,15,36",
"94,54,29,88,17,12,42,41,62,33,98",
"18,19,55,53,31,44,41,42,43",
"94,33,62,38,12,31,83,17,53,41,42,54,88,45,16,61,29,78,79",
"98,42,38,12,35,61,52,29,94,45,62,54,78,31,17",
"42,17,78,54,62,29,79,84,58,86,37,91,36,15,89,74,67,21,23",
"37,91,74,23,13,49,43,44,38",
"61,33,42,17,78,54,62,29,26,84,87,58,91",
"89,74,67,21,23,48,55,49,72,24,98,31,88,83,19",
"35,26,87,58,86,37,91,36,15,89,21,27,48,55,18,13,43",
"36,21,18,43,72,41,52",
"37,74,21,44,18,49,27,43,89,48,23,24,15,86,31,98,13",
"37,26,75,27,79,21,87,48,84,91,15,95,23,67,58,89,35,74,86,54,78",
"43,72,98,44,31,41,83,61,33,12,16,17,62",
"67,27,15,52,13,55,49,24,83,72,38,18,88,23,44,89,98,41,74",
"83,98,12,31,41,44,33,16,53,42,78,43,52,54,38,72,17,19,45,61,94,,62,24"
"21,23,27,38,98,13,15,83,48,89,67",
"33,44,83,35,45,78,19,75,42,61,31,88,12,52,54,79,26,17,62,41,53",
"13,43,98,94,38,41,83,19,45,53,12,16,78",
"98,49,94,83,61,41,48,55,19,23,31,27,88,24,44,67,45,72,52,38,21,,43,13"
"88,61,42,35,44,29,75",
"67,49,44,43,95,48,27,36,21,55,58,89,98,24,13",
"48,84,58,67,15,23,26,36,37,87,18,89,86,21,74,27,91,75,72,13,55,,95,43"
"24,87,55,89,72,86,91,49,95,37,13,15,18",
"31,98,23,55,48,45,44,72,94,67,88,38,83,49,61,13,43",
"88,31,53,38,42,52,55,19,61,43,24,49,44,45,12,72,18,41,94",
"62,29,35,75,84,87,58,37,89,23,27,55,18",
"98,18,38,23,31,48,55,13,19,45,61,41,83,53,27",
"12,45,52,88,33,38,27,43,61,94,72,83,44,18,19,31,48,53,24,41,98",
"19,41,35,84,42,54,79,52,33,62,31,88,45",
"21,23,27,48,55,18,49,72,24,98,94,44,31,38,41,83,19,61,33",
"79,35,75,26,84,86,37,95,15,89,74,21,23,18,49",
"72,18,74,13,87,75,58",
"15,89,21,27,13,72,24,41,83",
"94,62,16,31,19,88,33,75,29,38,61,41,83,35,53,45,42",
"87,91,21,29,23,35,78,86,48,67,84",
"79,75,36,29,67,35,78,89,58,17,86,15,95,12,74",
"16,86,53,62,35,36,89,95,15,87,42,75,74,58,29,17,37,91,26",
"83,27,52,55,94,88,74,49,89,48,98,18,13,19,24,41,31",
"38,29,26,41,17,45,62,84,87,33,61",
"31,94,43,13,41,44,83,33,72,49,18,55,19",
"49,43,31,52,88,19,61,33,12,42,54",
"87,58,86,37,91,36,95,15,89,67,23,48,55,18,13,49,24,98,94",
"54,88,17,94,33,19,38,78,42",
"52,88,83,19,45,33,53,12,16,42,17,78,54,62,29,35,75,26,84,87,58",
"83,19,61,53,42,17,78,54,62,29,79,35,75,84,87,58,86,37,91",
"19,83,23,31,45,18,61,88,33,52,43,94,24,72,98,55,53,49,48",
"61,38,12,48,44,55,18,33,19,13,98,53,43,52,31",
"12,16,42,78,62,79,35,58,37,95,15,74,67",
"91,24,84,74,89,37,23,86,36,21,58",
"88,19,45,61,33,53,12,16,42,17,78,54,62,29,79,35,75,26,84,87,58,,86,37"
"23,49,43,13,24,67,74,27,89,55,98,41,94,52,72,31,48,19,21,18,44,,88,38"
"78,79,35,37,36",
"31,88,83,19,45,61,33,53,12,16,17,78,54,62,79,35,75,26,84",
"27,98,55,31,38,23,18,43,95,67,88,15,74,52,13,41,49,72,21,94,48,,44,24"
"58,86,37,91,95,15,89,67,21,27,43,24,98,94,44",
"29,35,45,38,19,17,16,79,33,62,83,42,94,31,78,41,12,54,98,53,44",
"36,89,67,18,43,44,31",
"83,98,42,12,35,31,45,53,41,33,44",
"24,38,21,41,45,88,49,31,67,43,61,19,52,98,44,23,83",
"67,35,62,91,15,26,18,89,75",
"29,79,35,84,58,86,37,91,36,95,15,89,74,67,21,23,27,48,55,18,13",
"79,75,84,37,91,15,67,21,23,55,13",
"83,19,53,12,42,78,54,62,29,79,35,75,26,84,58,37,91",
"43,72,94,44,31,38,19,12,42,17,78,54,62",
"33,53,12,42,17,62,79,35,75,26,84,87,58,86,37,91,36,95,89",
"13,24,49,48,74,86,87,37,43,95,98,27,21,55,72,18,89",
"58,86,37,91,36,95,15,89,74,67,21,23,27,48,55,18,13,49,43,72,98,,94,44"
"61,35,16,91,37,26,53,12,86,17,75,83,87,33,78,42,58",
"54,62,29,79,35,75,26,58,86,91,95,89,74,21,23,27,48",
"86,37,91,89,67,21,23,27,48,18,49,43,72,24,98,94,31",
"18,24,31,98,27,44,52,61,19,43,72,67,41,94,55",
"26,27,62,87,18,75,86"
]

print(solve(ordering_rules, updates))  # Output: 143
