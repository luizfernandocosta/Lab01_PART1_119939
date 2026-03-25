from pathlib import Path

import kagglehub

from src.client.kaggle_client import KaggleClient
import logging
import os

class RawService:

    def __init__(self):
        pass

    def download_dataset(self):

        logging.info("downloading kaggle dataset")
        output_dir = f"{Path(__file__).parent.parent.parent}/data/raw"
        dataset_path = 'TMDB_movie_dataset_v11'

        path = kagglehub.dataset_download("asaniczka/tmdb-movies-dataset-2023-930k-movies", path=f"{dataset_path}.csv", output_dir=output_dir)

        logging.info("downloading kaggle dataset done")

        if os.path.exists(f"{Path(__file__).parent.parent.parent}/data/raw/.complete"):
            logging.info("removing .complete folder")
            try:
                os.remove(f"{Path(__file__).parent.parent.parent}/data/raw/.complete")
            except PermissionError:
                logging.info("permission error removing .complete folder, please remove folder manually")

        logging.info(f"dataset downloaded to {path}")

        if os.path.exists(f"{Path(__file__).parent.parent.parent}/data/raw/{dataset_path}.csv"):
            logging.info(f"renaming {dataset_path}.csv to movies.csv")
            os.rename(f"{Path(__file__).parent.parent.parent}/data/raw/{dataset_path}.csv", f"{Path(__file__).parent.parent.parent}/data/raw/movies.csv")
            logging.info("renaming done")

        logging.info("finished downloading dataset")

        return path

