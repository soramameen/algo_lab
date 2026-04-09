from search_core import GraphSearch
from problem import GridPathfinding


def DepthFristSearch(problem):
    return GraphSearch(problem, lambda node: -node.d)


if __name__ == "__main__":
    print("---深さ優先探索---")
    problem = GridPathfinding()
    path = DepthFristSearch(problem)
    if path is not None:
        print([str(n) for n in path])
    else:
        print(None)
