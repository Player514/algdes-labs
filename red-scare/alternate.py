from Parser import dataGen
from collections import deque


def dfs(s, t, edges):
    stack = deque([(s.name, s.color)])
    visited = set()
    path_map = {}
    while stack:
        current, current_color = deque.pop(stack)
        if current not in visited:
            visited.add(current)
            if current == t:
                return True
            if current in edges and edges[current]:
                for next in edges[current]:
                    if next in visited: 
                        continue
                    if current_color == "Red" and next.color == "Black" or \
                       current_color == "Black" and next.color == "Red":
                        path_map[next.name] = current
                        deque.appendleft(stack, (next.name, next.color))
    return False

def alternate():
    nodes_dictionary, _, start, end, edges_dict = dataGen()
    start = nodes_dictionary[start]
    is_alternating = dfs(start, end, edges_dict)
    print(is_alternating)

alternate()