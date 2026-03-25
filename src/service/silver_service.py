from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

def print_dataframe():
    logging.info("printing dataframe")
    df = pd.read_csv(f"{Path(__file__).parent.parent.parent}/data/raw/movies.csv")

    folderpath = f"{Path(__file__).parent.parent.parent}/data/silver/"

    table = pa.Table.from_pandas(df)

    logging.info(f"table schema: {table.schema}")

    if (not Path(folderpath).exists()):
        logging.info(f"creating folder: {folderpath}")
        Path(folderpath).mkdir(parents=True, exist_ok=True)

    logging.info("saving table to parquet:")
    pq.write_table(table, f"{folderpath}/movies.parquet")



    # print(df.dtypes)
    #
    # df["homepage"].isna().any()

    # print(df.head())

    # save_to_parquet(pa.Table.from_pandas(df.head()), "test.parquet")

def save_to_parquet(table: pa.Table, path: str):
    logging.info(f"saving table to parquet: {path}")
    pq.write_table(table, path)

def main():
    logging.info("starting silver layer")

    logging.info("cleaning dataset")

    logging.info("generating basic report for the dataset")

    logging.info("generating graphs")

    logging.info("saving dataset to parquet file")
