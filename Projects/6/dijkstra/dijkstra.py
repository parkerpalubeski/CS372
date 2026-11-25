import sys
import json
import math  # If you want to use math.inf for infinity


import netfuncs #Imported the file from the last project, just to keep things clean in this file



#find the next router (or "node" in the "graph")
def find_next_router(unvisited, distances):
    best_router = None
    best_distance = math.inf

    for router in unvisited:
        if distances[router] < best_distance:
            best_distance = distances[router]
            best_router = router

    return best_router

#build the shortest path from one router to another
def build_path(previous, start_router, end_router):
    if start_router == end_router:
        return [start_router]

    if previous[end_router] is None:
        return []

    path = []
    current = end_router
    while current is not None:
        path.append(current)
        if current == start_router:
            break
        current = previous[current]

    path.reverse()
    return path


def dijkstras_shortest_path(routers, src_ip, dest_ip):
    """
    This function takes a dictionary representing the network, a source
    IP, and a destination IP, and returns a list with all the routers
    along the shortest path.

    The source and destination IPs are **not** included in this path.

    Note that the source IP and destination IP will probably not be
    routers! They will be on the same subnet as the router. You'll have
    to search the routers to find the one on the same subnet as the
    source IP. Same for the destination IP. [Hint: make use of your
    find_router_for_ip() function from the last project!]

    The dictionary keys are router IPs, and the values are dictionaries
    with a bunch of information, including the routers that are directly
    connected to the key.

    This partial example shows that router `10.31.98.1` is connected to
    three other routers: `10.34.166.1`, `10.34.194.1`, and `10.34.46.1`:

    {
        "10.34.98.1": {
            "connections": {
                "10.34.166.1": {
                    "netmask": "/24",
                    "interface": "en0",
                    "ad": 70
                },
                "10.34.194.1": {
                    "netmask": "/24",
                    "interface": "en1",
                    "ad": 93
                },
                "10.34.46.1": {
                    "netmask": "/24",
                    "interface": "en2",
                    "ad": 64
                }
            },
            "netmask": "/24",
            "if_count": 3,
            "if_prefix": "en"
        },
        ...

    The "ad" (Administrative Distance) field is the edge weight for that
    connection.

    **Strong recommendation**: make functions to do subtasks within this
    function. Having it all built as a single wall of code is a recipe
    for madness.
    """
    #MODIFY HERE
    start_router = netfuncs.find_router_for_ip(routers, src_ip) #function calls from last project
    end_router = netfuncs.find_router_for_ip(routers, dest_ip)

    if start_router is None:
        print("start_router could not be found")
        return []
    elif end_router is None:
        print("end_router could not be found")
        return []

    weights = {router: math.inf for router in routers}
    previous = {router: None for router in routers}
    unvisited = set(routers.keys())

    weights[start_router] = 0

    while unvisited:
        current = find_next_router(unvisited, weights)

        if current is None or weights[current] == math.inf:
            break

        unvisited.remove(current)

        if current == end_router:
            break

        connections = routers[current].get("connections", {})
        for neighbor, conn_info in connections.items():
            if neighbor not in unvisited or neighbor not in weights:
                continue

            weight = conn_info["ad"]
            new_distance = weights[current] + weight

            if new_distance < weights[neighbor]:
                weights[neighbor] = new_distance
                previous[neighbor] = current

    return build_path(previous, start_router, end_router)
    pass

#------------------------------
# DO NOT MODIFY BELOW THIS LINE
#------------------------------
def read_routers(file_name):
    with open(file_name) as fp:
        data = fp.read()

    return json.loads(data)

def find_routes(routers, src_dest_pairs):
    for src_ip, dest_ip in src_dest_pairs:
        path = dijkstras_shortest_path(routers, src_ip, dest_ip)
        print(f"{src_ip:>15s} -> {dest_ip:<15s}  {repr(path)}")

def usage():
    print("usage: dijkstra.py infile.json", file=sys.stderr)

def main(argv):
    try:
        router_file_name = argv[1]
    except:
        usage()
        return 1

    json_data = read_routers(router_file_name)

    routers = json_data["routers"]
    routes = json_data["src-dest"]

    find_routes(routers, routes)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    
