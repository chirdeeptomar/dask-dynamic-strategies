"""True Evaluator Strategy"""
from dask.dataframe import DataFrame


def no_op_strategy(df: DataFrame) -> DataFrame:
    """Evaluates True is row is not None"""
    return df
