"""Represents the data saving step of the pipeline"""

from pprint import pprint
from dask.dataframe import DataFrame


def save(data: DataFrame):
    """Save enriched data to the target"""
    pprint("Saving enriched dataset")
    pprint(data.compute())
