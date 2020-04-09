## Imports

import networkx as nx
import matplotlib.pyplot as plt
import math

def read_names(file_name):
    names = []
    file = open(file_name, 'r')
    for line in file:
        names += [line.strip()]
    return names

# [A, B, 'C,D'] => returns 4
def prepare_G(names):
    total_count = 0
    for name in names:
        if ',' in name:
            total_count += 2
        else:
            total_count += 1
    
    # Initialize the graph
    G = nx.DiGraph()
    num_to_name = {}
    # insert nodes
    for i in range(len(names)):
        num_to_name[i] = names[i]
        G.add_node(i)

    for i in range(len(names)):
        for j in range(len(names)):
            if i != j:
                G.add_edge(i, j)
                
    return G, num_to_name, total_count

def find_solution(G, total_count, GROUP_SIZE, num_to_name):
    return G, 0


def plot_graph(G):
    nx.draw(G, with_labels=True, node_color='red', font_size=18, width=3,node_size=1000)


# take second element for sort
def takeSecond(elem):
    return elem[1]

def get_neighbors_who_are_not_any_group(host, already_visited, G):
    visitors = list(G.predecessors(host)) # get all the neighbors visited
    for i in already_visited:
        if i in visitors:
            visitors.remove(i)
    return visitors

def find_solution(G, total_count, group_size, num_to_names):
    num_groups = math.floor(total_count / group_size)
    if total_count % group_size != 0:
        num_groups += 1
    iteration = 0

    #O(e)
    while(G.number_of_edges() > 0):
        visited_hosts = []
        visited_nodes = []
        hosts_to_visitors = {}
        groups = 0

        # We will do this until we fill all the groups O(n)
        while(groups < num_groups):
        
            # sort the nodes by indegree ascending
            # TODO: runtime of sort? O(n log n)
            # TODO: indegree O(E)
            nodes_with_indegree = list(G.in_degree())
            nodes_with_indegree.sort(key=takeSecond, reverse=True)

            # pick one node 
            host, degree = nodes_with_indegree.pop(0)
            # TODO: runtime of get_neighbors_who_are_not_any_group O(E) because networkx uses adjacency list
            # representation, so the library probably needs to look at all of nodes that are toward the host.
            visitors = get_neighbors_who_are_not_any_group(host, visited_nodes, G)

            # check if the node is already a host, or all the neighbors are part of other groups
            # if fails, then pick another node. Keep searching
            # TODO: runtime of this loop O(n*E)
            while (host in visited_nodes or len(visitors) == 0) and len(nodes_with_indegree) > 0:
                host, degree = nodes_with_indegree.pop(0)
                visitors = get_neighbors_who_are_not_any_group(host, visited_nodes, G)

            # If there is no more hosts left, then we are DONE...
            if (len(nodes_with_indegree) == 0):
                break;

            # pick the neighbors to fill the group with group_size
            number_of_people_in_group = 2 if ("," in num_to_names[host]) else 1
            chosen_visitors = []
            # TODO: runtime of this loop O(E*N)
            while number_of_people_in_group < group_size:
                if (len(visitors) == 0):
                    break;
                visitor = visitors.pop(0)
                chosen_visitors += [visitor]
                # TODO: handle if a visitor is a couple
                number_of_people_in_group += 2 if ("," in num_to_names[visitor]) else 1

            # Remove the chosen edges (visitor, host) for all the chosen visitors
            # TODO: runtime of this loop O(e)
            for visitor in chosen_visitors:
                if G.has_edge(visitor, host):
                    G.remove_edge(visitor, host)

            visited_hosts += [host]
            visited_nodes += chosen_visitors
            visited_nodes += [host]
            groups += 1
            hosts_to_visitors[host] = chosen_visitors
        
#         print("Iteration ", iteration, ":", hosts_to_visitors)
#         print("Now manually filling the groups with unvisited nodes")
            
        # 1. Create a list of unvisited nodes = (nodes - visited_nodes) [1, 2, 3] - [1] 
        unvisited_nodes = []
        nodes = list(G.nodes)

        #O(n)
        # TODO: runtime of this loop
        for i in nodes:
            if i not in visited_nodes:
                unvisited_nodes += [i]
        # 2. Iterate through hosts_to_visitors (it's a dictionary). 
        # If the host + its visitors are less than group_size, then add some from unvisited_nodes until it becomes equal to group_size
        # O(n^2)
        for i in hosts_to_visitors:
            # TODO: handle if host/visitor is a couple
            number_of_people_in_group = 2 if ("," in num_to_names[i]) else 1
            for j in range(len(hosts_to_visitors[i])):
                number_of_people_in_group += 2 if ("," in num_to_names[j]) else 1

            while number_of_people_in_group < group_size:
                if len(unvisited_nodes) == 0:
                    break
                new_visitor = unvisited_nodes.pop(0)
                hosts_to_visitors[i].append(new_visitor)
                number_of_people_in_group += 2 if ("," in num_to_names[new_visitor]) else 1

        #3. If the total number of groups (look at variable 'groups') is less than num_groups, 
        #then create groups ('num_groups' - 'groups' many; for instance, if there are total 3 groups, 
        #but only 1 group made so far, then you need to create two more groups) using the rest of unvisited_nodes.
        # O(n^2)
        if groups < num_groups:
            for i in range(groups, num_groups):
                if len(unvisited_nodes) == 0:
                    break
                hostPerson = unvisited_nodes.pop(0)
                sizeOfHost = 2 if ("," in num_to_names[hostPerson]) else 1
                hosts_to_visitors[hostPerson] = []
                visitedPeopleAmount = 0
                while sizeOfHost + visitedPeopleAmount < group_size:
                    if len(unvisited_nodes) == 0:
                        break
                    visitor = unvisited_nodes.pop(0)
                    visitedPeopleAmount += 2 if ("," in num_to_names[visitor]) else 1
                    hosts_to_visitors[hostPerson].append(visitor)
            
        hosts_to_visitors_in_strings = {}
        for i in hosts_to_visitors:
            hosts_to_visitors_in_strings[num_to_names[i]] = [num_to_names[v] for v in hosts_to_visitors[i]]

        print("Iteration ", iteration, ":", hosts_to_visitors_in_strings)
        
        iteration += 1
    return G

def verify(G):
    # check G has no edges
    print("VERIFY RESULT:", G.number_of_edges() == 0)

def main():
    file_name = input("Type file name: ")
    group_size = int(input("Type number of people per group: "))
    
    # 1. Read the names and create array of names
    # File: A\n B\n C,D => ['A', 'B', 'C,D']
    names = read_names(file_name)
    
    # 2. Create a fully connected graph G
    # Number of nodes = 3 where couple is one node
    # Each node is indexed as 0, 1, 2
    # Also return num_to_name {0 => 'A', 1 => 'B', 2 => ['C', 'D']}
    # total_count = number of people = 4 people total
    G, num_to_name, total_count = prepare_G(names)
    print("Total", total_count)
    print("Names: ", num_to_name)

    # 3. run the algorithm
    # final_G is the graph created by the algorithm
    # G is the graph that should have no edges left
    G = find_solution(G, total_count, group_size, num_to_name)
    plot_graph(G)
    
    # 4. verify that final_G is empty
    verify(G)
    
main()