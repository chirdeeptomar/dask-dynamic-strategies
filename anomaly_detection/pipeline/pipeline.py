"""Main Pipeline"""

from pathlib import Path
from pprint import pprint
from typing import Callable

from dask.dataframe import DataFrame

from anomaly_detection.pipeline.steps import storage, loader, evaluator, enricher
from anomaly_detection.strategies.enrichment.no_op_strategy import no_op_strategy


def start_pipeline(path: Path, strategy: Callable[[DataFrame], DataFrame]) -> None:
    """Basic Pipeline"""
    pprint(f"Dataset Path: {path}")
    pprint(f"Strategy Name: {strategy.__name__}")

    data: DataFrame = loader.load(path)
    alerted_df = evaluator.evaluate(data, strategy)
    if alerted_df.size.compute() > 0:
        pprint(f"Enriching alerted dataset")
        enriched_data: DataFrame = enricher.enrich(alerted_df, no_op_strategy)
        storage.save(enriched_data)
