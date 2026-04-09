from search_core import GraphSearch
from problem import GridPathfinding


def WAstarSearch(problem, w=1.0):
    f = lambda node: problem.heuristic(node.state) * w + node.g
    return GraphSearch(problem, f)


if __name__ == "__main__":
    print("---WAstar---")
    problem = GridPathfinding()
    path = WAstarSearch(problem, w=5.0)
    if path is not None:
        print([str(n) for n in path])
    else:
        print(None)
