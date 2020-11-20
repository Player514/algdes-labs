import Parser as P
import re
import sys

sys.setrecursionlimit(5000)

class Node2:
  def __init__(self, name, color):
    self.name = name
    self.color = color
    self.cost = 9999999
    self.childrenname = []
  def getName(self):
      return self.name

  def getColor(self):
      return self.color

cache = []
cost = 0

def run(currentnodename,end,nodes_dictionary,cost):
    currentnode = nodes_dictionary[currentnodename]
    newcost = 0
    if(currentnode.color == 'Black'):
        newcost = cost
    else:
        newcost = cost + 1
    if(currentnode.cost > newcost):
        currentnode.cost = newcost
    for childname in currentnode.childrenname:
        if(nodes_dictionary[childname].cost > newcost):
            run(childname,end,nodes_dictionary,newcost)

def dataGen2():
    line1 = sys.stdin.readline().split()
    # print(line1)
    n = int(line1[0]) #number of vertices
    m = int(line1[1]) #number of edges
    r = int(line1[2]) #cardinality of R
    directed = True
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
        node = Node2(nodeName, color)
        nodesDictionary[nodeName.rstrip()] = node

    edges_dict = {}
    edges = []
    for x in range(0,m):
        i = sys.stdin.readline().split()
        if(directed):
            nodesDictionary[i[0]].childrenname.append(i[2]) 
            nodesDictionary[i[2]].childrenname.append(i[0]) 
        else:
            nodesDictionary[i[0]].childrenname.append(i[2])


    return nodesDictionary,sourceNode, sinkNode
    
def few():
    nodes_dictionary, startname, endname = dataGen2()
    start = nodes_dictionary[startname].cost = 0
    run(startname,endname,nodes_dictionary,0)
#    for name in nodes_dictionary:
#        print(nodes_dictionary[name].name,nodes_dictionary[name].cost)
    print(nodes_dictionary[endname].cost)
few()