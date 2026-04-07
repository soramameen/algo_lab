from argparse import Action


class StateSpaceProblem:
    def __init__(self):
        assert False

    def get_init_state(self):
        assert False

    def is_goal(self, state):
        assert False

    def get_available_actions(self,state):
        assert False

    def get_next_state(self,state,action):
        assert False

    def get_action_cost(self,state,action):
        assert False

    def heuristic(self,state):
        assert False

class GridState:
    def __init__(self, xy):
        self.x = xy[0]
        self.y = xy[1]

    def __hash__(self):
        return hash((self.x, self.y))
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return "(" + self.x.__str__() + ", " + self.y.__str__() + ")"

class GridPathfinding(StateSpaceProblem):
    state_type = GridState
    def __init__(self, width = 5, height = 5, init_position = (0,0), goal_position = (4,4)):
        self.width = width
        self.height = height
        self.init_position = init_position
        self.goal_position = goal_position

        self.init_state = GridState(init_position)

    def get_init_state(self):
        return self.init_state

    def is_goal(self, state):
        return (state.x == self.goal_position[0]) and (state.y == self.goal_position[1])

    def get_available_actions(self,state):
        actions = []
        if state.x > 0:
            actions.append('l')
        if state.x < self.width - 1:
            actions.append('r')
        if state.y > 0:
            actions.append('u')
        if state.y < self.height - 1:
            actions.append('d')
        return actions

    def get_next_state(self,state,action):
        if action == 'l':
            return GridState((state.x - 1,state.y))
        elif action == 'r':
            return GridState((state.x + 1,state.y))
        elif action == 'u':
            return GridState((state.x,state.y - 1))
        elif action == 'd':
            return GridState((state.x,state.y+1))

# 木探索
class SearchNode:
    def __init__(self, state):
        self.state = state

    def set_g(self,g):
        self.g = g

    def set_d(self,d):
        self.d = d

    def set_prev_n(self, prev_n):
        self.prev_n = prev_n

    def __str__(self):
        return self.state.__str__() + ": g=" + str(self.g) + ", d=" + str(self.d)

    def get_path(self):
        cur_node = self
        path = []

        while (cur_node is not None and hasattr(cur_node, 'prev_n')):
            path.append(cur_node)
            cur_node = cur_node.prev_n


def TreeSearch(problem, priority_f=None):
    open = []

    init_state = problem.get_init_state()
    init_node = SearchNode(init_state)
    init_node.set_g(0)
    init_node.set_d(0)

    logger = SearchLogger()
    logger.start()

    open.append(init_node)

    while (len(open) > 0):
        open.sort(key=lambda node: priority_f(node), reverse=True)

        node = open.pop()
        logger.expanded += 1

        if problem.is_goal(node.state):
            logger.end()
            logger.print()
            return node.get_path()

        else:
            actions = problem.get_available_actions(node.state)

            for a in actions:
                next_state = problem.get_next_state(node.state, a)
                next_node = SearchNode(next_state)
                next_node.set_g(node.g + problem.problem.get_action_cost(next_state, a))
                next_node.set_d(node.d + 1)
                next_node.set_prev_n(node)
                open.append(next_node)
                logger.generated += 1

        logger.end()
        logger.print()
        return None

def is_explored(node, closed_list):
    for n in closed_list:
        if (n.state == node.state) and (n.g <= node.g):
            return True
    return False

def GraphSearch(problem, priority_f=None):
    open = []
    closed = []

    init_state = problem.get_init_state()
    init_node = SearchNode(init_state)
    init_node.set_g(0)
    init_node.set_d(0)

    logger = SearchLogger()
    logger.start()

    open.append(init_node)
    closed.append(init_node)

    while (len(open) > 0):
        open.sort(key=lambda node: priority_f(node), reverse=True)

        node = open.pop()
        logger.expanded += 1

        if problem.is_goal(node.state):
            logger.end()
            logger.print()
            return node.get_path()
        else:
            actions = problem.get_available_actions(node.state)

            for a in actions:
                next_state = problem.get_next_state(node.state, a)

                next_node = SearchNode(next_state)
                next_node.set_g(node.g + problem.get_action_cost(next_state, a))

                next_node.set_d(node.d + 1)
                if not is_explored(next_node, closed):
                    next_node.set_prev_n(node)
                    open.append(next_node)
                    closed.append(next_node)
                    logger.generated += 1
                else:
                    logger.pruned += 1
    logger.end()
    logger.print()
    return None

if __name__ == '__main__':
    breathFirstSearch = Breath

def BreadthFirstSearch(problem):
    return GraphSearch(problem, lambda node: node.d)

def DepthFirstSearch(problem):
    return GraphSearch(problem, lambda node: -node.d)

def DikstraSearch(problem):
    return GraphSearch(problem, lambda node: node.g)

logger = SearchLogger()

def RecursiveSearchEngine(problem, cur_node):
    logger.expanded += 1

    if problem.is_goal(cur_node.state):
        return [cur_node]
    else:
        actions = problem.get_available_actions(cur_node.state)

        for a in actions:
            next_state = problem.get_next_state(cur_node.state, a)

            next_node = SearchNode(next_state)
            next_node.set_g(cur_node.g + problem.problem.get_action_cost(next_state, a))

            next_node.set_d(cur_node.d + 1)
            next_node.set_prev_n(cur_node)

            logger.generated += 1
            path = RecursiveSearchEngine(next_node, cur_node)
            if len(path) > 0:
                path.append(cur_node)
                return path
    return []

def RecursiveDepthFirstSearch(problem):
    init_state = problem.get_init_state()
    init_node = SearchNode(init_state)
    init_node.set_g(0)
    init_node.set_d(0)

    logger.start()

    path = RecursiveSearchEngine(init_node, init_node)

    logger.end()
    logger.print()

    return path

import time

class SearchLogger:
    def __init__(self):
        self.expanded = 0
        self.generated = 0
        self.pruned = 0

    def start(self):
        self.start_perf_time = time.perf_counter()
        self.start_time = time.time()

    def end(self):
        self.end_perf_time = time.perf_counter()
        self.end_time = time.time()

    def branching_factor(self):
        return self.generated/self.expanded

    def pruned_rate(self):
        return self.pruned/(self.generated + self.expanded)

    def time(self):
        return self.end_time - self.start_time

    def perf_time(self):
        return self.end_perf_time - self.start_perf_time

    def expansion_rate(self):
        return self.expanded/self.time()

    def generation_rate(self):
        return self.generated / self.time()

    def print(self):
        print("Time: ", self.time())
        print("Perf Time: ", self.perf_time())
        print("Expanded: ", self.expanded)
        print("Generated: ", self.generated)
        print("Pruned: ", self.pruned)
        print("Expansion rate: ", self.expansion_rate())
        print("Generation rate: ", self.generation_rate())
        print("Branching factor: ", self.branching_factor())
        print("Pruned rate: ", self.pruned_rate())
