"""True Evaluator Strategy"""

from dask.dataframe import DataFrame


def symbol_name_eval_strategy(sdf: DataFrame) -> DataFrame:
    """Evaluates True is row is not None"""
    df = sdf[sdf["Symbol"].str.contains('AA')]
    return df
