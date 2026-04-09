from problem import StateSpaceProblem, GridState, GridPathfinding
from search_core import (
    SearchNode,
    SearchLogger,
    logger,
    TreeSearch,
    GraphSearch,
    is_explored,
    RecursiveSearchEngine,
    RecursiveDepthFirstSearch,
)
from breadth_first_search import BreadthFristSearch
from depth_first_search import DepthFristSearch
from dijkstra import DijkstraSearch
from astar import AstarSearch
from wastar import WAstarSearch
from greedy_best_first import GreedyBestFirstSearch


if __name__ == "__main__":
    print("---daikijkstra----")
    problem = GridPathfinding()
    path = DijkstraSearch(problem)
    if path is not None:
        print([str(n) for n in path])
    else:
        print(None)

    print("---Astar---")
    problem = GridPathfinding()
    path = AstarSearch(problem)
    if path is not None:
        print([str(n) for n in path])
    else:
        print(None)

    print("---WAstar---")
    problem = GridPathfinding()
    path = WAstarSearch(problem, w=5.0)
    if path is not None:
        print([str(n) for n in path])
    else:
        print(None)
