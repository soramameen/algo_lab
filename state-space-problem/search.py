"""探索アルゴリズム（BFS, A*）を定義する。"""

from __future__ import annotations

import heapq
from collections import deque
from dataclasses import dataclass, field
from typing import Any

from base import StateSpaceProblem


@dataclass
class SearchResult:
    """探索結果をまとめるデータクラス。"""

    found: bool
    actions: list[Any] = field(default_factory=list)
    states: list[Any] = field(default_factory=list)
    cost: float = 0.0
    expanded: int = 0

    def summary(self) -> str:
        lines: list[str] = []
        lines.append(f"解の有無: {'あり' if self.found else 'なし'}")
        if self.found:
            lines.append(f"アクション列: {self.actions}")
            lines.append(f"状態列: {[repr(s) for s in self.states]}")
            lines.append(f"コスト: {self.cost}")
        lines.append(f"展開ノード数: {self.expanded}")
        return "\n".join(lines)


def bfs(problem: StateSpaceProblem) -> SearchResult:
    """幅優先探索を行う。

    Returns
    -------
    SearchResult
        探索結果（解の有無、アクション列、状態列、コスト、展開数）。
    """
    init = problem.get_init_state()
    # 状態 → (直前状態, アクション, 累積コスト)
    visited: dict[Any, tuple[Any, Any, float]] = {init: (None, None, 0.0)}
    queue: deque[Any] = deque([init])
    expanded = 0

    while queue:
        state = queue.popleft()
        expanded += 1

        if problem.is_goal(state):
            return _build_result(visited, state, expanded)

        for action in problem.get_available_actions(state):
            next_state = problem.get_next_state(state, action)
            if next_state not in visited:
                cost = visited[state][2] + problem.get_action_cost(state, action)
                visited[next_state] = (state, action, cost)
                queue.append(next_state)

    return SearchResult(found=False, expanded=expanded)


def astar(problem: StateSpaceProblem) -> SearchResult:
    """A* 探索を行う。

    ヒューリスティクスには problem.heuristic() を使用する。

    Returns
    -------
    SearchResult
        探索結果。
    """
    init = problem.get_init_state()
    g_score: dict[Any, float] = {init: 0.0}
    # (f, counter, state) — counter で tie-break
    counter = 0
    open_heap: list[tuple[float, int, Any]] = [(problem.heuristic(init), counter, init)]
    # 状態 → (直前状態, アクション)
    came_from: dict[Any, tuple[Any, Any]] = {init: (None, None)}
    closed: set[Any] = set()
    expanded = 0

    while open_heap:
        _f, _c, state = heapq.heappop(open_heap)

        if state in closed:
            continue
        closed.add(state)
        expanded += 1

        if problem.is_goal(state):
            return _build_result_astar(came_from, g_score, state, expanded)

        for action in problem.get_available_actions(state):
            next_state = problem.get_next_state(state, action)
            if next_state in closed:
                continue
            tentative_g = g_score[state] + problem.get_action_cost(state, action)
            if tentative_g < g_score.get(next_state, float("inf")):
                g_score[next_state] = tentative_g
                came_from[next_state] = (state, action)
                f = tentative_g + problem.heuristic(next_state)
                counter += 1
                heapq.heappush(open_heap, (f, counter, next_state))

    return SearchResult(found=False, expanded=expanded)


def _build_result(
    visited: dict[Any, tuple[Any, Any, float]],
    goal: Any,
    expanded: int,
) -> SearchResult:
    """BFS 用: visited 辞書から経路を再構築する。"""
    actions: list[Any] = []
    states: list[Any] = []
    cost = visited[goal][2]
    state = goal
    while True:
        prev, action, _c = visited[state]
        states.append(state)
        if action is not None:
            actions.append(action)
        if prev is None:
            break
        state = prev
    actions.reverse()
    states.reverse()
    return SearchResult(
        found=True, actions=actions, states=states, cost=cost, expanded=expanded
    )


def _build_result_astar(
    came_from: dict[Any, tuple[Any, Any]],
    g_score: dict[Any, float],
    goal: Any,
    expanded: int,
) -> SearchResult:
    """A* 用: came_from 辞書から経路を再構築する。"""
    actions: list[Any] = []
    states: list[Any] = []
    state = goal
    while True:
        prev, action = came_from[state]
        states.append(state)
        if action is not None:
            actions.append(action)
        if prev is None:
            break
        state = prev
    actions.reverse()
    states.reverse()
    return SearchResult(
        found=True,
        actions=actions,
        states=states,
        cost=g_score[goal],
        expanded=expanded,
    )
