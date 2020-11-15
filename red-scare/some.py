import queue
from Parser import dataGen, printNodeDictionary, printEdges


def path_to_map(path):
    fr = path[0]
    path_map = {}
    for i in range(1, len(path)):
        path_map[fr] = path[i]
        fr = path[i]
    return path_map

def BFS(s, t):
    global found_path
    q = queue.Queue()
    explored = set()
    q.put([s])

    while not q.empty():
        path = q.get()
        node = path[-1]
        explored.add(node)
        for _to_node in edges_dict[node]:
            to_node = _to_node.getName()

            if to_node not in explored and capacities[node][to_node] > flows[node][to_node]:
                new_path = path.copy() + [to_node]
                q.put(new_path)
                if to_node == t:
                    found_path = path_to_map(new_path)
                    return True
    return False


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


# def to_output():
#     m = 0
#     active_flows = []
#     for fr, adjs in enumerate(adjacents):
#         for to in adjs:
#             if flows[fr][to] > 0:
#                 m += 1
#                 if capacities[fr][to] > 0:
#                     active_flows.append((fr, to))
#
#     print(len(flows), f, m)
#     for el in active_flows:
#         fr, to = el
#         print(fr, to, flows[fr][to])
#

nodesDictionary, edges, s, t, edges_dict = dataGen()
# print("source", s, "sink", t)
# printEdges(edges)
found_path = {}
capacities = {}
flows = {}
f = 0
for s_node in edges_dict:
    capacities[s_node] = {}
    flows[s_node] = {}
    for e_node in edges_dict[s_node]:
        capacity = 1 if e_node.getColor() == "Red" else 2

        capacities[s_node][e_node.getName()] = capacity
        flows[s_node][e_node.getName()] = 0
# printEdges(edges)
# printNodeDictionary(nodesDictionary)

has_path = BFS(s, t)
while has_path:
    min_flow = float("+Inf")
    for fr in found_path:
        to = found_path[fr]
        flow = capacities[fr][to] - flows[fr][to]
        if flow < min_flow:
            min_flow = flow
    res = push_flow(found_path, min_flow)
    if res:
        print("true")
        break

    has_path = BFS(s, t)

if not res:
    print("false")