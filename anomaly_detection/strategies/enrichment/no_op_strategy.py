"""True Evaluator Strategy"""
from dask.dataframe import DataFrame


def no_op_strategy(df: DataFrame) -> DataFrame:
    """No-Op strategy for enrichment"""
    return df
