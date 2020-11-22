import queue
from Parser import dataGen, printNodeDictionary, printEdges, add_node, add_edge, remove_edge, is_graph_directed
from shared import print_d

import time
import sys


class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


sys.stdout = Unbuffered(sys.stdout)


def logger():
    global count
    global stop_threads
    print("Start logger")
    prevCount = 0
    while not stop_threads:
        print(count - prevCount, "/ second", count)
        prevCount = count
        time.sleep(1)


def modify_graph(nodesDictionary, edges, s, t, edges_dict):
    nodesDictionaryCopy = nodesDictionary
    edges_dict_copy = edges_dict
    edges = []
    edges_dict = {}
    nodesDictionary = {}

    for n, currentNode in nodesDictionaryCopy.items():
        name = currentNode.getName()
        color = currentNode.getColor()
        inNode = add_node(nodesDictionary, name + '_in', color)
        outNode = add_node(nodesDictionary, name + '_out', color)
        add_edge(edges, edges_dict, inNode, outNode)

    for n, currentNode in nodesDictionaryCopy.items():
        if n in edges_dict_copy:
            for node in edges_dict_copy[n]:
                from_node = currentNode.getName() + '_out'
                to_node = node.getName() + '_in'
                add_edge(edges, edges_dict, nodesDictionary[from_node], nodesDictionary[to_node])

    print_d("Setting up new starting & ending points")

    new_s = 'NEW_STARTING_NODE'
    new_t = 'NEW_ENDING_NODE'

    new_starting_node = add_node(nodesDictionary, new_s, 'Black')
    new_ending_node = add_node(nodesDictionary, new_t, 'Black')

    add_edge(edges, edges_dict, new_starting_node, nodesDictionary[s + '_in'])
    add_edge(edges, edges_dict, new_starting_node, nodesDictionary[t + '_in'])

    return nodesDictionary, edges, edges_dict, new_s, new_t, new_ending_node, new_starting_node


def contract_graph(nodesDictionary, edges, s, t, edges_dict):
    q = queue.Queue()
    explored = set()
    q.put(s)
    originalLength = len(nodesDictionary)

    def remove_node(n):
        neighbouring_edges = edges_dict[n]
        node_to_remove = nodesDictionary[n]
        print_d("Remove", n)
        for node in edges_dict[n]:
            for node2 in edges_dict[node.getName()]:
                print_d(node.getName(), '->', node2.getName())
                if node2 == node_to_remove:
                    print_d("Remove this edge!")
                    edges_dict[node.getName()].remove(node2)
                    if node.getName() not in explored:
                        q.put(node.getName())

        add_edge(edges, edges_dict, neighbouring_edges[0], neighbouring_edges[1])
        add_edge(edges, edges_dict, neighbouring_edges[1], neighbouring_edges[0])
        del edges_dict[n]
        del nodesDictionary[n]

    def is_contractible(n):
        return n != s and n != t and len(edges_dict[n]) == 2 and nodesDictionary[n].getColor() != "Red"

    while not q.empty():
        n = q.get()
        if n in edges_dict:
            for _new_to in edges_dict[n]:
                new_to = _new_to.getName()
                if new_to not in explored:
                    if is_contractible(new_to):
                        remove_node(new_to)

    return originalLength != len(nodesDictionary)


def to_path_map(path, s, t):
    re_path = [t]

    while re_path[-1] != s:
        re_path.append(path[re_path[-1]])
    re_path = [idx_to_name[x] for x in re_path]
    re_path.reverse()

    fr = re_path[0]
    path_map = {}
    for i in range(1, len(re_path)):
        path_map[fr] = re_path[i]
        fr = re_path[i]

    return path_map


def BFS(s, t):
    found_path = [-1] * len(nodesDictionary)
    q = queue.Queue()
    explored = set()
    q.put(s)

    while not q.empty():
        node = q.get()
        explored.add(node)
        if node not in edges_dict:
            continue
        print_d(node, [x.getName() for x in edges_dict[node]])
        adj_edges = edges_dict[node]
        for _to_node in adj_edges:
            to_node = _to_node.getName()

            if to_node not in explored and capacities[node][to_node] > flows[node][to_node]:
                to_node_idx = name_to_idx[to_node]
                node_idx = name_to_idx[node]
                found_path[to_node_idx] = node_idx
                q.put(to_node)
                if to_node == t:
                    return to_path_map(found_path, name_to_idx[s], name_to_idx[t])
    return None


def push_flow(path, flow):
    for fr in found_path:
        to = found_path[fr]

        flows[fr][to] += flow
        flows[to][fr] -= flow
        # adjacents[to].add(fr)
    # print(f'pushed {flow}')

    if flow == 2:
        return False
    else:
        return True


def get_all_red_nodes():
    node_set = set()
    for j, n in nodesDictionary.items():
        if n.getColor() == 'Red' and n.getName().endswith('_in'):
            node_set.add((j, n))
    return node_set


nodesDictionary, edges, s, t, edges_dict = dataGen()

contract_graph(nodesDictionary, edges, s, t, edges_dict)

if is_graph_directed():
    print("?!")
    exit()

nodesDictionary, edges, edges_dict, new_s, new_t, new_ending_node, new_starting_node = modify_graph(nodesDictionary,
                                                                                                    edges, s, t,
                                                                                                    edges_dict)

name_to_idx = {}
idx_to_name = {}
for i, n in enumerate(nodesDictionary):
    name_to_idx[n] = i
    idx_to_name[i] = n

edge_to_end = None
red_nodes = get_all_red_nodes()
for i, node in red_nodes:
    print_d("Current goal node: ", node.getName(), node.getColor())
    print_d("Creating edge from", node.getName(), "to new_ending_node")

    remove_edge(edges, edges_dict, edge_to_end)
    edge_to_end = add_edge(edges, edges_dict, node, new_ending_node)

    print_d("Setting up capacities and flows")

    f = 0
    capacities = {}
    flows = {}
    for n in nodesDictionary:
        capacities[n] = {}
        flows[n] = {}

    for s_node in edges_dict:
        for e_node in edges_dict[s_node]:
            capacity = 1 if e_node is not new_ending_node else 2
            capacities[s_node][e_node.getName()] = capacity
            flows[s_node][e_node.getName()] = 0
            capacities[e_node.getName()][s_node] = capacity
            flows[e_node.getName()][s_node] = 0

    print_d("RUN")

    found_path = BFS(new_s, new_t)
    print_d(found_path)
    while found_path is not None:
        min_flow = float("+Inf")
        for fr in found_path:
            to = found_path[fr]
            flow = capacities[fr][to] - flows[fr][to]
            if flow < min_flow:
                min_flow = flow
        f += push_flow(found_path, min_flow)

        found_path = BFS(new_s, new_t)

    if f == 2:
        print(True)
        exit()
print(False)
