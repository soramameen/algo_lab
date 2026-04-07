# algo_lab

## 状態空間問題 — グリッド経路探索 CLI

`state-space-problem/` に状態空間探索の CLI を実装しています。

### ファイル構成

```
state-space-problem/
  base.py    StateSpaceProblem 抽象基底クラス
  grid.py    GridState / GridPathfinding（グリッド経路探索）
  search.py  BFS / A* 探索アルゴリズム
  main.py    CLI 入口
```

### 実行例

**デフォルト（引数なしで BFS、デフォルト壁あり）:**

```bash
python state-space-problem/main.py
```

デフォルトでは 5x5 グリッドに壁 `(0,2) (1,2) (2,4) (3,4) (3,1) (4,1)` が配置され、ジグザグ経路を誘導する迷路風レイアウトになります。

**BFS（幅優先探索）:**

```bash
python state-space-problem/main.py bfs --rows 5 --cols 5 --start 0,0 --goal 4,4
```

**A\* 探索（壁あり）:**

```bash
python state-space-problem/main.py astar --rows 5 --cols 5 --start 0,0 --goal 4,4 --walls "0,2 1,2 2,4 3,4 3,1 4,1"
```

**アニメーション付き（経路を 1 手ずつ表示）:**

```bash
python state-space-problem/main.py bfs --rows 5 --cols 5 --start 0,0 --goal 4,4 --animate
```

**アニメーション速度を変更:**

```bash
python state-space-problem/main.py astar --rows 7 --cols 7 --start 0,0 --goal 6,6 --walls "0,2 1,2 2,4 3,4 3,1 4,1" --animate --delay 0.3
```

**実行結果の例（デフォルト壁あり）:**

```
解の有無: あり
アクション列: ['Down', 'Down', 'Right', 'Right', 'Down', 'Down', 'Right', 'Right']
状態列: ['(0, 0)', '(1, 0)', '(2, 0)', '(2, 1)', '(2, 2)', '(3, 2)', '(4, 2)', '(4, 3)', '(4, 4)']
コスト: 8.0
展開ノード数: 18
```

### オプション

| オプション   | 既定値 | 説明                          |
| ------------ | ------ | ----------------------------- |
| `algorithm`  | `bfs`  | `bfs` または `astar`（省略時は `bfs`） |
| `--rows`     | 5      | グリッドの行数                |
| `--cols`     | 5      | グリッドの列数                |
| `--start`    | 0,0    | 開始位置 (`row,col`)          |
| `--goal`     | 4,4    | 目的位置 (`row,col`)          |
| `--walls`    | (0,2) (1,2) (2,4) (3,4) (3,1) (4,1) | 壁 `"r1,c1 r2,c2 ..."`。`--walls ""` で壁なし |
| `--animate`  | off    | 経路を 1 手ずつ ASCII アニメーション表示 |
| `--delay`    | 0.15   | アニメーション各フレーム間隔（秒） |

**アニメーション表示記号:**

| 記号 | 意味       |
| ---- | ---------- |
| `S`  | 開始位置   |
| `G`  | 目的位置   |
| `#`  | 壁         |
| `*`  | 経路       |
| `@`  | 現在位置   |
| `.`  | 空きセル   |