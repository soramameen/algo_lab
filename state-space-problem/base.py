"""状態空間問題の抽象基底クラスを定義する。"""

from abc import ABC, abstractmethod
from typing import Any


class StateSpaceProblem(ABC):
    """状態空間探索問題の抽象基底クラス。

    具体問題はこのクラスを継承し、各メソッドを実装すること。
    """

    @abstractmethod
    def get_init_state(self) -> Any:
        """初期状態を返す。"""

    @abstractmethod
    def is_goal(self, state: Any) -> bool:
        """state が目的状態かどうかを返す。"""

    @abstractmethod
    def get_available_actions(self, state: Any) -> list:
        """state で実行可能なアクションのリストを返す。"""

    @abstractmethod
    def get_next_state(self, state: Any, action: Any) -> Any:
        """state に action を適用した次状態を返す。"""

    @abstractmethod
    def get_action_cost(self, state: Any, action: Any) -> float:
        """state から action を実行するコストを返す。"""

    def heuristic(self, state: Any) -> float:
        """state から目的までの推定コストを返す（デフォルトは 0）。"""
        return 0
