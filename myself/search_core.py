import time


class SearchNode:
    def __init__(self, state):
        self.state = state

    def set_g(self, g):
        self.g = g

    def set_d(self, d):
        self.d = d

    def set_prev_n(self, prev_n):
        self.prev_n = prev_n

    def __str__(self):
        return self.state.__str__() + ": g=" + str(self.g) + ", d=" + str(self.d)

    def get_path(self):
        cur_node = self
        path = []

        while cur_node is not None and hasattr(cur_node, "prev_n"):
            path.append(cur_node)
            cur_node = cur_node.prev_n

        return path


def TreeSearch(problem, priority_f=None):
    open = []

    init_state = problem.get_init_state()
    init_node = SearchNode(init_state)
    init_node.set_g(0)
    init_node.set_d(0)

    logger = SearchLogger()
    logger.start()

    open.append(init_node)

    while len(open) > 0:
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
                next_node.set_g(node.g + problem.get_action_cost(node.state, a))
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

    while len(open) > 0:
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
                next_node.set_g(node.g + problem.get_action_cost(node.state, a))

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
        return self.generated / self.expanded

    def pruned_rate(self):
        return self.pruned / (self.generated + self.expanded)

    def time(self):
        return self.end_time - self.start_time

    def perf_time(self):
        return self.end_perf_time - self.start_perf_time

    def expansion_rate(self):
        return self.expanded / self.time()

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
            next_node.set_g(cur_node.g + problem.get_action_cost(cur_node.state, a))

            next_node.set_d(cur_node.d + 1)
            next_node.set_prev_n(cur_node)

            logger.generated += 1
            path = RecursiveSearchEngine(problem, next_node)
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

    path = RecursiveSearchEngine(problem, init_node)

    logger.end()
    logger.print()

    return path
