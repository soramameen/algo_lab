from search_core import GraphSearch
from problem import GridPathfinding


def DijkstraSearch(problem):
    return GraphSearch(problem, lambda node: node.g)


if __name__ == "__main__":
    print("---daikijkstra----")
    problem = GridPathfinding()
    path = DijkstraSearch(problem)
    if path is not None:
        print([str(n) for n in path])
    else:
        print(None)
