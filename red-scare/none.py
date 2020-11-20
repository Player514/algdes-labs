from Parser import dataGen
from collections import deque


def dfs(s, t, edges):
    stack = deque([s.name])
    visited = set()
    path_map = {}
    while stack:
        current = deque.popleft(stack)
        if current not in visited:
            visited.add(current)
            if current == t:
                return True
            if current in edges and edges[current]:
                for next in edges[current]:
                    if next in visited: 
                        continue
                    path_map[next.name] = current
                    deque.appendleft(stack, next.name)
    return False

def none():
    nodes_dictionary, _, start, end, edges_dict = dataGen()
    nodes_dictionary = {k:v for (k,v) in nodes_dictionary.items() if 'Black' in v.color}
    edges_dict = { k_:filtered for (k_, filtered) in {k:list(filter(lambda n: 'Black' in n.color, v)) for (k,v) in edges_dict.items()}.items() if filtered }
    
    if start not in nodes_dictionary: 
        print(-1)
    else:
        start = nodes_dictionary[start]
        path_exists = dfs(start, end, edges_dict)
        print(1 if path_exists else -1)

none()