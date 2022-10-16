"""Application Runner"""
from pathlib import Path

from dask.distributed import Client

from anomaly_detection.strategies.anomaly.market_category_strategy import market_category_eval_strategy
from anomaly_detection.strategies.anomaly.symbol_name_strategy import symbol_name_eval_strategy
from anomaly_detection.pipeline.pipeline import start_pipeline

DASK_CLUSTER = "localhost:8786"

if __name__ == "__main__":
    path = Path("../data/nasdaq-listed.csv")
    client = Client(DASK_CLUSTER)
    client.compute(start_pipeline(path, symbol_name_eval_strategy))
