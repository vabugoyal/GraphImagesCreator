# created by me
from . import simulation
import os


def simulateGraph(request):
    """
    This will return a tuple
    1. valid graph
    2. message
    3. number of stages in the graph
    """

    # clearing all the files inside output before running the function
    dir = 'static/output'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

    ALGOS = ["dfs", "bfs", "dijkstra", "kruskal", "prim"]
    numberofnodes = request.GET.get('nodes', '')
    algo = request.GET.get('algo', '').lower()
    try:
        numberofnodes = int(numberofnodes)
    except:
        return

    if (numberofnodes == 0):
        return

    if (algo not in ALGOS): return

    givenEdgeString = request.GET.get('edges', '').strip()
    givenEdgeStrings = givenEdgeString.split("\n")
    if (givenEdgeStrings[0] == ''): givenEdgeStrings = []

    g = [] # this will store edges

    nodes = list(range(1, numberofnodes + 1))
    print(givenEdgeStrings)
    print(nodes)
    print(algo)
    for R in givenEdgeStrings:
        try:
            x = list(map(int, R.split()))
            if (len(x) == 2):
                if (algo not in ["dfs", "bfs"]): return
                u, v = x
                if (not u in nodes) or (not v in nodes): return
                g.append(x)
            elif (len(x) == 3):
                if algo in ["dfs", "bfs"]: return
                u, v, w = x
                if (algo == "dijkstra") and w < 0: return
                if (not u in nodes) or (not v in nodes): return
                g.append(x)
            else:
                return
        except:
            return

    print(g)


    simulation.start(g, numberofnodes, algo.lower())
