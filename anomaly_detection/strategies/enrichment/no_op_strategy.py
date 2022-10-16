"""True Evaluator Strategy"""
from dask.dataframe import DataFrame


def no_op_strategy(row: DataFrame) -> DataFrame:
    """Evaluates True is row is not None"""
    return row
