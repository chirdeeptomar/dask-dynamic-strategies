"""Strategy Evaluator"""
from typing import Callable

from dask.dataframe import DataFrame


def evaluate(data: DataFrame, strategy: Callable[[DataFrame], DataFrame]) -> DataFrame:
    return strategy(data)
