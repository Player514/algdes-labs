from Parser import dataGen
from shared import print_d
import sys
import threading
import time

sys.setrecursionlimit(5000)


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


def max_edges(n):
    if n <= 1:
        return 1
    return n ** 2 - max_edges(n - 1)


count = 0


def BFS(s, t):
    def rec_bfs(node, t, has_red, explored):
        global count
        count += 1
        if node == t:
            if has_red:
                print("True")
                exit()
            return
        elif nodesDictionary[node].getColor() == 'Red':
            has_red = True

        explored.add(node)
        if node in edges_dict:
            adj_edges = edges_dict[node]
            for _to_node in adj_edges:
                to_node = _to_node.getName()
                if to_node not in explored:
                    rec_bfs(to_node, t, has_red, set(explored))

    rec_bfs(s, t, False, set())


nodesDictionary, edges, s, t, edges_dict = dataGen()

max_edge = max_edges(len(nodesDictionary))
statusStep = max_edge // 2
print(statusStep)
print_d("Setting up new starting & ending points")

print_d("Setting up capacities and flows")

print_d("RUN")

# printNodeDictionary(nodesDictionary)
# printEdges(edges)

import signal


def signal_handler(sig, frame):
    global stop_threads
    print('You pressed Ctrl+C!')
    stop_threads = True
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

stop_threads = False
threading.Thread(target=logger).start()

BFS(s, t)
print(False)
