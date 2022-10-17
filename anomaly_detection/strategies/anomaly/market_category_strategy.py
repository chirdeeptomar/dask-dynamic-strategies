"""True Evaluator Strategy"""


from dask.dataframe import DataFrame


def market_category_eval_strategy(sdf: DataFrame) -> DataFrame:
    """Evaluates True is row is not None"""
    return sdf[sdf["Market Category"] == 'G']
