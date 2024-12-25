from collections import defaultdict

# Function to find the largest clique in the network
def find_largest_clique(network):
    # Result variable to store the largest clique found
    largest_clique = []

    def backtrack(clique, candidates):
        nonlocal largest_clique  # Use nonlocal to modify the outer variable
        if not candidates:
            if len(clique) > len(largest_clique):
                largest_clique = clique
            return
        
        for member in list(candidates):  # Use list to avoid runtime changes
            new_candidates = candidates.intersection(network[member])
            backtrack(clique + [member], new_candidates)

    # Set of all nodes for the initial call
    nodes = set(network.keys())
    for node in nodes:
        new_candidates = nodes - {node}  # Exclude current node from candidates
        backtrack([node], new_candidates)

    return largest_clique

# Main logic
if __name__ == "__main__":
    # Read the input file with connections
    try:
        with open('problem_23/input_22.txt', 'r') as file:
            connections = [line.strip() for line in file]

        # Build the graph
        network = defaultdict(set)
        for connection in connections:
            a, b = connection.split('-')
            network[a].add(b)
            network[b].add(a)

        # Find the largest clique
        largest_clique = find_largest_clique(network)
        
        # Format the result
        if largest_clique:
            password = ",".join(sorted(largest_clique))  # Sort for consistency
            print(f"Password to the LAN party: {password}")
        else:
            print("No clique found.")

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")