"""Represents the data loading step of the pipeline"""

from pathlib import Path

import dask.dataframe as dd
from dask.dataframe import DataFrame


def load(path: Path) -> DataFrame:
    """Loads data from a source"""
    csv_data: DataFrame = dd.read_csv(path)
    return csv_data
