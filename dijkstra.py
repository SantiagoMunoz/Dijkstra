import collections
import math
import heapq
import csv
import sys

# Node list fields... 'name', 'outgoing_routes', 'incoming_routes', 'cost'
Route = collections.namedtuple('Route', ['origin', 'destination','cost'])

def load_data(routes_filename):
    nodes = {}
    route_list = []
    with open(routes_filename) as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            route_list.append(Route(row[0].strip(),row[1].strip(), int(row[2])))
    for route in route_list:
        if not route.origin in nodes.keys():
            nodes[route.origin] = ([route.origin, [], [], math.inf])
        if not route.destination in nodes.keys():
            nodes[route.destination] = ([route.destination, [], [], math.inf])
        nodes[route.origin][1].append(route)
        nodes[route.destination][2].append(route)
    return nodes

def dijkstra(node_list, origin, destination):
    unvisited_nodes = []
    node_list[origin][3] = 0;
    for node_name in node_list.keys():
        if node_name == destination:
            continue;
        unvisited_nodes.append([0 if node_name == origin else math.inf, node_name])
    # Calculate processed nodes
    while (len(unvisited_nodes) > 0):
        active_node = heapq.heappop(unvisited_nodes)  #Takes the lowest one
        if node_list[active_node[1]][3] > node_list[destination][3]:
            continue
        for route in node_list[active_node[1]][1]:
            this_cost = node_list[active_node[1]][3] + route.cost
            if this_cost < node_list[route.destination][3]:
                node_list[route.destination][3] = this_cost
                heapq.heappush(unvisited_nodes, [this_cost, route.destination])

    # Break down list of jumps that need to be taken
    current_node = destination;
    solution = []
    while(current_node != origin):
        candidate_route = Route("", "", math.inf)
        candidate_cost = math.inf
        for route in node_list[current_node][2]:
            if node_list[route.origin][3] < candidate_cost and route.cost == (node_list[current_node][3] - node_list[route.origin][3]):
                candidate_route = route
                candidate_cost = node_list[route.origin][3]
        solution.append(candidate_route);
        current_node = candidate_route.origin
    return solution

def print_solution(solution):
    cummulative_cost = 0
    while len(solution) > 0:
        hop = solution.pop()
        print(hop.origin + " -> " + hop.destination)
        cummulative_cost += hop.cost
    print("Total cost: " + str(cummulative_cost))

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: " + sys.argv[0] + " filename origin destination")
        print("Example: " + sys.argv[0] + " sample_paths.csv a c")
        exit(-1)
    nodes = load_data(sys.argv[1].strip())
    origin = sys.argv[2].strip()
    destination = sys.argv[3].strip()
    solution = dijkstra(nodes, origin, destination)
    print_solution(solution);
