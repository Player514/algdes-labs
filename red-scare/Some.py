from SimpleParser import parse
import queue

def BFS(s, t):
    global delta
    global from_path
    q = queue.Queue()
    explored = set()
    q.put(s)

    while not q.empty():
        node = q.get()
        explored.add(node)
        print(from_path)
        for to_node in adjacents[node]:
            if (capacities[node][to_node] < delta):
                continue
            if (to_node not in explored and capacities[node][to_node] > flows[node][to_node]):
                from_path[to_node] = node
                q.put(to_node)
                if (to_node == t):
                    return True
    return False

def push_flow(path, min_flow):
    for i in range(0, len(path) - 1):
        i2 = i + 1
        fr = path[i]
        to = path[i2]

        flows[fr][to] += min_flow
        flows[to][fr] -= min_flow
        adjacents[to].add(fr)
    print(f'pushed {min_flow}')
    return min_flow

def to_output():
    m = 0
    active_flows = []
    for fr, adjs in enumerate(adjacents):
        for to in adjs:
            if flows[fr][to] > 0:
                m += 1
                if capacities[fr][to] > 0:
                    active_flows.append((fr, to))

    print(len(flows), f, m)
    for el in active_flows:
        fr, to = el
        print(fr, to, flows[fr][to])


capacities, adjacents, flows, reds, s, t = parse()
from_path = [-1] * len(flows)
f = 0

delta = 2 ** 31
while delta > 0:
    has_path = BFS(s, t)
    while(has_path):
        to = from_path[t]
        path = [t, to]
        min_flow = capacities[to][t] - flows[to][t]
        while (to != s):
            fr = from_path[to]
            path.append(fr)
            diff = capacities[fr][to] - flows[fr][to]
            if (diff < min_flow):
                min_flow = diff
            to = fr
        path.reverse()
        f += push_flow(path, min_flow)

        has_path = BFS(s, t)
    print(has_path, delta)
    delta //= 2

to_output()
