# slides/

CLRS (Introduction to Algorithms) の学習スライド置き場。

## 主要スライド一覧

| ファイル | 内容 |
|----------|------|
| `growth-of-functions.md` | 第3章: 関数の増加度 (Θ/O/Ω/o/ω) |
| `merge-sort-divide-and-conquer.md` | §2.3: Merge Sort と分割統治法 |
| `visual-storyboard.md` | スライドのビジュアル方針・カラーパレット |

## ディレクトリ構成

| パス | 役割 |
|------|------|
| `docs/` | 原文資料・参照用（スライド本文ではない、編集不可） |
| `images/` | 図ファイル（`.mmd` と `.svg` のペアで管理） |
| `plans/` | 作業計画ファイル |

## 図の管理方法

図は Mermaid (`.mmd`) で作成し、`mmdc` で SVG に変換して使用する。

```bash
mmdc -i images/<name>.mmd -o images/<name>.svg
```

- `.mmd` がソース、`.svg` が生成物
- 常にペアで存在させる
- ファイル先頭に `%% ID:` コメントを記載

## 現状

- Phase 1（§2.3 図 3点 + 第3章図 2点）: 完了
- Phase 2（漸近記法の関係図 + 多項式/指数比較図）: 完了
- Phase 3（精密グラフ化）: 未着手
