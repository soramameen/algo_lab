from search_core import GraphSearch
from problem import GridPathfinding


def GreedyBestFirstSearch(problem):
    h = lambda node: problem.heuristic(node.state)
    return GraphSearch(problem, h)


if __name__ == "__main__":
    print("---Greedy Best First---")
    problem = GridPathfinding()
    path = GreedyBestFirstSearch(problem)
    if path is not None:
        print([str(n) for n in path])
    else:
        print(None)
