"""Strategy Factory"""
import enum
from typing import Callable

from anomaly_detection.strategies.anomaly import market_category_strategy, symbol_name_strategy

_ANOMALY_STRATEGIES = {
    'market_category': market_category_strategy.market_category_eval_strategy,
    'symbol_name': symbol_name_strategy.symbol_name_eval_strategy,
}


class StrategyType(enum.Enum):
    """Enum to represent strategy types"""
    ANOMALY = enum.auto()
    ENRICH = enum.auto


def get_strategy(name: str, strategy_type: StrategyType) -> Callable:
    """Factory method to get a Strategy function"""
    return _ANOMALY_STRATEGIES.get(name) if strategy_type == StrategyType.ANOMALY else None
