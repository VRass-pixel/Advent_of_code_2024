import re
import itertools
from collections import defaultdict

# Function to find all sets of 3 inter-connected computers
def find_triples(connections):
    network = defaultdict(set)
    
    for connection in connections:
        a, b = connection.split('-')
        network[a].add(b)
        network[b].add(a)

    triples = []
    for a, b, c in itertools.combinations(network.keys(), 3):
        if b in network[a] and c in network[a] and c in network[b]:
            triples.append(sorted([a, b, c]))
    
    return triples

# Function to filter triples containing at least one computer starting with 't'
def filter_triples(triples):
    return [triple for triple in triples if any(computer.startswith('t') for computer in triple)]

# Main logic
if __name__ == "__main__":
    with open ('problem_23/input_22.txt', 'r') as file:
        connections = [line.strip() for line in file]
        triples = find_triples(connections)
        filtered_triples = filter_triples(triples)
        
        print(f"Total triples containing at least one 't': {len(filtered_triples)}")
        #for triple in filtered_triples:
        #    print(triple)
