"""状態空間問題 CLI 入口。

Usage:
    python state-space-problem/main.py                          # 既定: bfs, 5x5, デフォルト壁あり
    python state-space-problem/main.py bfs  --rows 5 --cols 5 --start 0,0 --goal 4,4
    python state-space-problem/main.py astar --rows 5 --cols 5 --start 0,0 --goal 4,4 --walls "0,2 1,2 2,4 3,4 3,1 4,1"
    python state-space-problem/main.py bfs  --rows 5 --cols 5 --start 0,0 --goal 4,4 --animate --delay 0.15
"""

from __future__ import annotations

import argparse
import shutil
import sys
import time
from pathlib import Path

# state-space-problem ディレクトリを import パスに追加
sys.path.insert(0, str(Path(__file__).resolve().parent))

from grid import GridPathfinding
from search import SearchResult, astar, bfs

ALGORITHMS = {
    "bfs": bfs,
    "astar": astar,
}

# デフォルト壁配置（5x5, start=(0,0), goal=(4,4) で必ず解ける配置）
# 中央付近に壁を配置し、ジグザグ経路を誘導する迷路風レイアウト
DEFAULT_WALLS: set[tuple[int, int]] = {
    (0, 2),
    (1, 2),  # 上部縦壁: 右へ回り込ませる
    (2, 4),
    (3, 4),  # 右側縦壁: 左へ回り込ませる
    (3, 1),
    (4, 1),  # 下部縦壁: 右へ回り込ませる
}


def parse_pair(value: str) -> tuple[int, int]:
    """'row,col' 形式の文字列をタプルに変換する。"""
    parts = value.split(",")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError(
            f"'{value}' は 'row,col' 形式で指定してください"
        )
    return int(parts[0]), int(parts[1])


def parse_walls(value: str) -> list[tuple[int, int]]:
    """'r1,c1 r2,c2 ...' 形式の壁リストをパースする。"""
    pairs: list[tuple[int, int]] = []
    for token in value.split():
        pairs.append(parse_pair(token))
    return pairs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="状態空間問題 — グリッド経路探索 CLI",
    )
    parser.add_argument(
        "algorithm",
        nargs="?",
        default="bfs",
        choices=sorted(ALGORITHMS),
        help="探索アルゴリズム (bfs / astar)。省略時は bfs (既定: bfs)",
    )
    parser.add_argument("--rows", type=int, default=5, help="グリッドの行数 (既定: 5)")
    parser.add_argument("--cols", type=int, default=5, help="グリッドの列数 (既定: 5)")
    parser.add_argument(
        "--start",
        type=parse_pair,
        default=(0, 0),
        help="開始位置 'row,col' (既定: 0,0)",
    )
    parser.add_argument(
        "--goal", type=parse_pair, default=(4, 4), help="目的位置 'row,col' (既定: 4,4)"
    )
    parser.add_argument(
        "--walls",
        type=parse_walls,
        default=None,
        const="",
        nargs="?",
        help='壁の位置 "r1,c1 r2,c2 ..."（引用符で囲むこと）。省略時は迷路風デフォルト壁を使用',
    )
    parser.add_argument(
        "--animate",
        action="store_true",
        default=False,
        help="経路発見後に 1 手ずつグリッドをアニメーション表示する",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.15,
        help="アニメーション各フレームの間隔（秒）。既定: 0.15",
    )
    return parser


def animate_path(
    problem: GridPathfinding,
    result: SearchResult,
    delay: float = 0.15,
) -> None:
    """探索結果の経路を 1 手ずつターミナルにアニメーション表示する。"""
    if not result.found:
        print("\n（解なし — アニメーションなし）")
        return

    states = result.states
    path_set: set[tuple[int, int]] = set()
    term_h = shutil.get_terminal_size().lines

    for i, state in enumerate(states):
        path_set.add((state.row, state.col))
        # 画面クリア + 描画
        if term_h > 0:
            sys.stdout.write("\033[H\033[J")
        current = (state.row, state.col)
        frame = problem.render(path=path_set, current=current)
        step_label = f"Step {i + 1}/{len(states)}"
        sys.stdout.write(f"{step_label}\n{frame}\n")
        sys.stdout.flush()
        time.sleep(delay)

    # 最終フレーム: 現在位置マーカーを外して経路全体を表示
    if term_h > 0:
        sys.stdout.write("\033[H\033[J")
    sys.stdout.write(f"Path complete ({len(states)} states)\n")
    sys.stdout.write(problem.render(path=path_set) + "\n")
    sys.stdout.flush()


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    # --walls が明示されなかった場合はデフォルト壁を使用
    if args.walls is None:
        walls_set = set(DEFAULT_WALLS)
    else:
        walls_set = set(args.walls) if args.walls else set()

    problem = GridPathfinding(
        rows=args.rows,
        cols=args.cols,
        start=args.start,
        goal=args.goal,
        walls=walls_set,
    )

    search_fn = ALGORITHMS[args.algorithm]
    result = search_fn(problem)
    print(result.summary())

    if args.animate:
        print()  # サマリーとアニメーションの間に空行
        animate_path(problem, result, delay=args.delay)


if __name__ == "__main__":
    main()
