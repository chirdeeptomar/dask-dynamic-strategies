"""Application Runner"""
import sys

from pathlib import Path
from pprint import pprint

from dask.distributed import Client

from strategies.factory import get_strategy, StrategyType
from anomaly_detection.pipeline.pipeline import start_pipeline

DASK_CLUSTER = "localhost:8786"

if __name__ == "__main__":
    strategy_to_apply = sys.argv[1]
    strategy = get_strategy(strategy_to_apply, StrategyType.ANOMALY)
    if strategy:
        path = Path("../data/nasdaq-listed.csv")
        client = Client(DASK_CLUSTER)
        client.compute(start_pipeline(path, strategy))
    else:
        pprint("Strategy not found.")
