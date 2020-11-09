def parse():
    nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    adjacents = [
            [1],
            [2],
            [3],
            [4],
            [5],
            [6],
            [7],
            [8],
            [9],
            []
            ]
    reds = { 1, 5, 8 }
    s = 0
    t = 10
    capacities = [[0] * len(nodes) for x in nodes]
    flows = [[0] * len(nodes) for x in nodes]
    for i, _nodes in enumerate(adjacents):
        for node in _nodes:
            if (node in reds):
                capacities[i][node] = float('+Inf')
            else:
                capacities[i][node] = 1

    return capacities, adjacents, flows, reds, s, t
