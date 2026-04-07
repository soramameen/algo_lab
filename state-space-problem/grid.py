"""グリッド上の経路探索問題を定義する。"""

from __future__ import annotations

from dataclasses import dataclass

from base import StateSpaceProblem


@dataclass(frozen=True)
class GridState:
    """グリッド上の位置を表す状態。"""

    row: int
    col: int

    def __repr__(self) -> str:
        return f"({self.row}, {self.col})"


# 4 方向の移動アクション
ACTIONS: dict[str, tuple[int, int]] = {
    "Up": (-1, 0),
    "Down": (1, 0),
    "Left": (0, -1),
    "Right": (0, 1),
}


class GridPathfinding(StateSpaceProblem):
    """グリッド上の経路探索問題。

    Parameters
    ----------
    rows : int
        グリッドの行数。
    cols : int
        グリッドの列数。
    start : tuple[int, int]
        開始位置 (row, col)。
    goal : tuple[int, int]
        目的位置 (row, col)。
    walls : set[tuple[int, int]] | None
        通過不可能な座標の集合。
    """

    def __init__(
        self,
        rows: int,
        cols: int,
        start: tuple[int, int],
        goal: tuple[int, int],
        walls: set[tuple[int, int]] | None = None,
    ) -> None:
        if rows <= 0 or cols <= 0:
            raise ValueError("rows と cols は正の整数である必要があります")
        for label, (r, c) in (("開始位置", start), ("目的位置", goal)):
            if not (0 <= r < rows and 0 <= c < cols):
                raise ValueError(
                    f"{label} ({r},{c}) がグリッド範囲外です (rows={rows}, cols={cols})"
                )
        for w in walls or set():
            wr, wc = w
            if not (0 <= wr < rows and 0 <= wc < cols):
                raise ValueError(
                    f"壁の位置 ({wr},{wc}) がグリッド範囲外です "
                    f"(rows={rows}, cols={cols})"
                )
        self.rows = rows
        self.cols = cols
        self.start = GridState(*start)
        self.goal = GridState(*goal)
        self.walls: set[tuple[int, int]] = walls or set()
        for pos in (start, goal):
            if pos in self.walls:
                raise ValueError(f"開始または目的位置が壁と重複しています: {pos}")

    def get_init_state(self) -> GridState:
        return self.start

    def is_goal(self, state: GridState) -> bool:
        return state == self.goal

    def get_available_actions(self, state: GridState) -> list[str]:
        actions: list[str] = []
        for name, (dr, dc) in ACTIONS.items():
            nr, nc = state.row + dr, state.col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if (nr, nc) not in self.walls:
                    actions.append(name)
        return actions

    def get_next_state(self, state: GridState, action: str) -> GridState:
        if action not in ACTIONS:
            raise ValueError(f"未知のアクション: {action}")
        dr, dc = ACTIONS[action]
        return GridState(state.row + dr, state.col + dc)

    def get_action_cost(self, state: GridState, action: str) -> float:
        return 1.0

    def heuristic(self, state: GridState) -> float:
        """マンハッタン距離によるヒューリスティクス。"""
        return abs(state.row - self.goal.row) + abs(state.col - self.goal.col)

    # -- 描画ヘルパー --------------------------------------------------

    def render(
        self,
        path: set[tuple[int, int]] | None = None,
        current: tuple[int, int] | None = None,
    ) -> str:
        """グリッドを ASCII 文字で描画して返す。

        Parameters
        ----------
        path : set[tuple[int, int]] | None
            経路として表示する座標集合。
        current : tuple[int, int] | None
            現在位置（アニメーション用）。

        表示記号:
            S  開始位置
            G  目的位置
            #  壁
            *  経路（開始/目標/現在位置を除く）
            @  現在位置
            .  空きセル
        """
        path = path or set()
        start_t = (self.start.row, self.start.col)
        goal_t = (self.goal.row, self.goal.col)
        lines: list[str] = []
        for r in range(self.rows):
            cells: list[str] = []
            for c in range(self.cols):
                pos = (r, c)
                if pos == current:
                    cells.append("@")
                elif pos == start_t:
                    cells.append("S")
                elif pos == goal_t:
                    cells.append("G")
                elif pos in self.walls:
                    cells.append("#")
                elif pos in path:
                    cells.append("*")
                else:
                    cells.append(".")
            lines.append(" ".join(cells))
        return "\n".join(lines)
