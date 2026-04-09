from search_core import GraphSearch
from problem import GridPathfinding


def AstarSearch(problem):
    f = lambda node: problem.heuristic(node.state) + node.g
    return GraphSearch(problem, f)


if __name__ == "__main__":
    print("---Astar---")
    problem = GridPathfinding()
    path = AstarSearch(problem)
    if path is not None:
        print([str(n) for n in path])
    else:
        print(None)
