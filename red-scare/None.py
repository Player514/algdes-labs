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
    for x in range(0,n):
        nodeName = sys.stdin.readline().rstrip("\n")
        color = "Black"
        if '*' in nodeName:
            color = "Red"
            nodeName = nodeName.rstrip("*").rstrip()
        node = Node(nodeName, color)
        nodesDictionary.update({nodeName.rstrip() : node})

    edges = []
    for x in range(0,m):
        i = sys.stdin.readline().split()
        node1 = nodesDictionary.get(i[0])
        node2 = nodesDictionary.get(i[2])
        edge = Edge(node1, node2)
        edges.append(edge)

    return (nodesDictionary, edges, sourceNode, sinkNode)

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


def printGraph(graph):
    for x, y in graph.items():
        edgesString =""
        for i in y:
            edgesString = edgesString + "(" + i.getNode1().getName() + "," + i.getNode2().getName() + ")"
        print("          (",x.getName(),",", x.getColor(),"),", edgesString )
    print("\n")

def addEdge(graph, edge, node):
    if node in graph:
        edges = graph.get(node)
    else:
        edges = []
    edges.append(edge)
    graph.update({node : edges})
    return graph

def buildBlackGraph(edges, sourceNode, sinkNode):
    graph = {}
    for x in edges:
        if (x.getNode1().getColor() == "Black" and x.getNode2().getColor() == "Black"):
            graph = addEdge(graph, x, x.getNode1())
            graph = addEdge(graph, x, x.getNode2())
        elif x.getNode1() == sourceNode:
            graph = addEdge(graph, x, x.getNode1())
            graph = addEdge(graph, x, x.getNode2())
        elif x.getNode2() == sinkNode :
            graph = addEdge(graph, x, x.getNode1())
            graph = addEdge(graph, x, x.getNode2())

    return graph

#following getpath code is build upon Amalie Anderson kattis hand-in: WaifUntilDark
def getpath(parrentalDictionary, sourceNode, sinkNode):
    path = []
    path.append(sinkNode)
    if parrentalDictionary == None:
        return []
    else:
        x = parrentalDictionary.get(sinkNode)
        while not (x == sourceNode):
            path.append(x)
            x = parrentalDictionary.get(x)
        path.append((sourceNode))
        return path

#following BFS code is build upon Amalie Anderson kattis hand-in: WaifUntilDark
def BFS(graph, sourceNode, sinkNode):
    if not (sourceNode in graph) or not (sinkNode in graph):
        return -1
    else:
        parrentalDictionary = {}
        #Discovered is a list, that holds a node once it has been visited
        discovered = {sourceNode}
        queue = [sourceNode]
        while len(queue) > 0:
            inspectingNode = queue.pop(0)
            for x in graph.get(inspectingNode):
                if not (x.getNode2() in discovered):
                    if x.getNode2() == sinkNode:
                        parrentalDictionary.update({sinkNode : inspectingNode})
                        return len(getpath(parrentalDictionary, sourceNode, sinkNode))
                    else:
                        queue.append(x.getNode2())
                        discovered.add(x.getNode2())
                        parrentalDictionary.update({x.getNode2() : inspectingNode})
    return -1


nodesDictionary, edges, sourceNodeName, sinkNodeName = dataGen()
sourceNode = nodesDictionary.get(sourceNodeName)
sinkNode = nodesDictionary.get(sinkNodeName)
graph = buildBlackGraph(edges, sourceNode, sinkNode)
count = BFS(graph, sourceNode, sinkNode)
print("The lenght of the shortest path from ", sourceNodeName, "to", sinkNodeName, "is ", count)
