"""Strategy Factory"""
import enum
from typing import Callable

from anomaly_detection.strategies.anomaly.market_category_strategy import market_category_eval_strategy
from anomaly_detection.strategies.anomaly.symbol_name_strategy import symbol_name_eval_strategy

_ANOMALY_STRATEGIES = {
    'market_category': market_category_eval_strategy,
    'symbol_name': symbol_name_eval_strategy,
}


class StrategyType(enum.Enum):
    ANOMALY = enum.auto()
    ENRICH = enum.auto


def get_strategy(name: str, strategy_type: StrategyType) -> Callable:
    return _ANOMALY_STRATEGIES.get(name) if strategy_type == StrategyType.ANOMALY else None
