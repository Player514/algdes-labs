import re
import sys




class Node:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def getName(self):
      return self.name

  def getColor(self):
      return self.color




class Edge:
  def __init__(self, node1, node2):
    self.node1 = node1
    self.node2 = node2

  def getNode1(self):
      return self.node1

  def getNode2(self):
      return self.node2





def dataGen():
    line1 = sys.stdin.readline().split()
    n = int(line1[0]) #number of vertices
    m = int(line1[1]) #number of edges
    r = int(line1[2]) #cardinality of R

    sourceNode, sinkNode = sys.stdin.readline().split()

    # the node dictionary maps the name of a node with a node instance
    nodesDictionary = {}
    redNodes = []
    for x in range(0,n):
        nodeName = sys.stdin.readline().rstrip("\n")
        color = "Black"
        if '*' in nodeName:
            color = "Red"
            nodeName = nodeName.rstrip("*").rstrip()
        node = Node(nodeName, color)
        nodesDictionary.update({nodeName.rstrip() : node})

    edges_dict = {}
    edges = []
    for x in range(0,m):
        i = sys.stdin.readline().split()
        node1 = nodesDictionary.get(i[0])
        node2 = nodesDictionary.get(i[2])
        edge = Edge(node1, node2)
        edges.append(edge)
        if node1.name in edges_dict:
            edges_dict[node1.name].append(node2)
        else:
            edges_dict[node1.name] = [node2]
        if i[1] != "->":
            if node2.name in edges_dict:
                edges_dict[node2.name].append(node1)
            else:
                edges_dict[node2.name] = [node1]

    return nodesDictionary, edges, sourceNode, sinkNode, edges_dict

def printNodeDictionary(nodesDictionary):
    print("Nodes:")
    for x, y in nodesDictionary.items():
        print(y.getName(), y.getColor())
    print("\n\n\n\n\n")

def printEdges(edges):
    print("Edges:")
    for x in edges:
        print(x.getNode1().getName(), x.getNode2().getName())
    print("\n\n\n\n\n\n")


# nodesDictionary, edges, startNode, endNode = dataGen()
# print("sourceNode:", startNode,"sinkNode:", endNode, "\n")
# printNodeDictionary(nodesDictionary)
# printEdges(edges)
