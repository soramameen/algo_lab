from search_core import GraphSearch
from problem import GridPathfinding


def BreadthFristSearch(problem):
    return GraphSearch(problem, lambda node: node.d)


if __name__ == "__main__":
    print("---幅優先探索---")
    problem = GridPathfinding()
    path = BreadthFristSearch(problem)
    if path is not None:
        print([str(n) for n in path])
    else:
        print(None)
