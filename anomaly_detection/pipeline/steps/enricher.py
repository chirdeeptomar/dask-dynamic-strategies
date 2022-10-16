"""Represents the data enrichment step of the pipeline"""
import logging
from typing import Callable

from dask.dataframe import DataFrame


logger = logging.getLogger(__file__)


def enrich(row_data: DataFrame, func: Callable[[DataFrame], DataFrame]) -> DataFrame:
    """Enrichment Function"""
    return func(row_data)
