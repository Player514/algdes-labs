import sys
import math
import re 
import time


def parse_stdin(): 
    points = []
    for line in sys.stdin:
        line = line.strip()

        point_match = re.search('^\s*(?P<first>\w+)\s*(?P<second>([-+]?\d+(\.\d+)?([eE]?\+\d+)?))\s*(?P<third>([-+]?\d+(\.\d+)?([eE]?\+\d+)?))$', line)
        if point_match: 
            name = point_match.group("first")
            x = float(point_match.group("second"))
            y = float(point_match.group("third"))
            point = (name, x, y)
            points.append(point)
    return points


def dist(x1,y1,x2,y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    
class Node:
    def __init__(self,p,left,right,cmp_x, isLeaf):
        self.name = p[0]
        self.x = p[1]
        self.y = p[2]
        self.cmp_x = cmp_x
        self.left = left
        self.right = right
        self.isLeaf = isLeaf

    def __lt__(self,other):
        if self.cmp_x:
            if self.x != other.x:
                return self.x < other.x
            else:
                return self.y < other.y

        else:
            if self.y != other.y:
                return self.y < other.y
            else:
                return self.x < other.x

    def __eq__(self,other):
        if other.x == self.x and other.y == self.y:
            return True
        else:
            return False
            
def create_kdtree(k, isX):
    if not k:
        return
    if isX:
        k.sort(key=lambda n: n[1])
    else:
        k.sort(key=lambda n: n[2])
    median = len(k) // 2
    left = create_kdtree(k[:median], not isX)
    right = create_kdtree(k[median+1:], not isX)
    return Node(k[median], left, right, isX, False)

def nn(node, point, isX):
    px = point[1]
    py = point[2]
    if node is None:
        return None, None
    if node.name is point[0]:
        return None, None
    closest = node
    closest_dist = dist(node.x, node.y, px, py)
    
    if isX:
        if px < node.x:
            branch = node.left
        else:
            branch = node.right
        new_node, new_closest_dist = nn(branch, point, not isX)
    else:
        if py < node.y:
            branch = node.left
        else:
            branch = node.right
        new_node, new_closest_dist = nn(branch, point, not isX)
    
    if new_closest_dist != None and new_closest_dist < closest_dist:
        closest_dist = new_closest_dist
        closest = new_node
        
    return closest, closest_dist

points = parse_stdin()
node = create_kdtree(points, True)

closest = (Node(('temp', 0,0), None, None, True, True),999999999)
for p in points:
    res = nn(node, p, True)
    if res[0] is None:
        continue
    if(res[1] < closest[1]):
        closest = res
end = time.time()
print(closest[1])
