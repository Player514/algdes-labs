import sys
import re
import math

def euclidean_distance(first, second): 
    x1, y1 = first[1], first[2]
    x2, y2 = second[1], second[2]
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def parse_stdin(): 
    points = []
    regex = re.compile('^\s*(?P<name>\w+)\s*(?P<x>([-+]?\d+(\.\d+)?([eE]?\+\d+)?))\s*(?P<y>([-+]?\d+(\.\d+)?([eE]?\+\d+)?))$')
    for line in sys.stdin:
        line = line.strip()
        point_match = regex.search(line)
        if point_match: 
            name = point_match.group('name')
            x = float(point_match.group('x'))
            y = float(point_match.group('y'))
            points.append((name, x, y))

    return points


def find_closest(input: list):
    if len(input) == 2:
        first = input[0]
        second = input[1]
        return (first, second)

    if len(input) == 3: 
        closest = (None, None)
        shortest_distance = float('inf')
        for first in range(0,3):
            for second in range(first + 1, 3):
                first_point = input[first]
                second_point = input[second]
                distance = euclidean_distance(first_point, second_point)
                if distance < shortest_distance:
                    shortest_distance = distance
                    closest = (first_point, second_point)
        return closest

    split = int(len(input)/2)
    split_left = input[0:split]
    split_right = input[split:len(input)]

    left_closest = find_closest(split_left)
    right_closest = find_closest(split_right)

    delta = min(euclidean_distance(left_closest[0], left_closest[1]), euclidean_distance(right_closest[0], right_closest[1]))
    include = []
    split_candidate = input[split]
    for index in range(0, split):
        i = -index
        first_candidate = input[split-index-1]
        second_candidate = input[split+index]
        if euclidean_distance(first_candidate, second_candidate) < delta: 
            include.append(first_candidate)
            include.append(second_candidate)

    include = sorted(include, key=lambda point: point[2])
    closest = (None, None)
    shortest_distance = float('inf')
    for index, s in enumerate(include):
        iterations = 15
        for s_ in include[index + 1:]:
            if iterations == 0: 
                continue
            distance = euclidean_distance(s, s_)
            if distance < shortest_distance:
                shortest_distance = distance
                closest = (s, s_)
            iterations -= 1

    if closest[0] and closest[1] and euclidean_distance(closest[0], closest[1]) < delta:
        return closest

    return left_closest if euclidean_distance(left_closest[0], left_closest[1]) < euclidean_distance(right_closest[0], right_closest[1]) else right_closest

points = parse_stdin()
points = sorted(points, key=lambda point: point[1])
closest = find_closest(points)
print(closest[0][0], euclidean_distance(closest[0], closest[1]))