import logging
from pathlib import Path

import psycopg
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import numpy as np

from src.dataclass.database_dataclass import DatabaseDataclass


class GoldService:

    pass

    def __init__(self, database_config: DatabaseDataclass):
        self.database_config = database_config

    def connect_to_database(self):
        db_host = self.database_config.db_host
        db_name = self.database_config.db_name
        db_user = self.database_config.db_user
        db_password = self.database_config.db_password

        logging.info(f"connecting to database: {db_host}/{db_name}")

        conn = psycopg.connect(f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}")
        logging.info("connected to database")

        return conn

    def create_schema(self):
        logging.info("creating schema")
        conn = self.connect_to_database()
        cur = conn.cursor()
        cur.execute("""
            CREATE SCHEMA IF NOT EXISTS tmdb;
        """)
        logging.info("schema created")
        conn.commit()
        cur.close()

    def create_table(self):
        logging.info("creating table")
        conn = self.connect_to_database()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tmdb.movies (
                id BIGSERIAL PRIMARY KEY,
                movie_id BIGINT,
                title TEXT,
                vote_average DOUBLE PRECISION,
                vote_count BIGINT,
                status TEXT,
                release_date DATE,
                revenue BIGINT,
                runtime INTEGER,
                adult BOOLEAN,
                backdrop_path TEXT,
                budget BIGINT,
                homepage TEXT,
                imdb_id TEXT,
                original_language TEXT,
                original_title TEXT,
                overview TEXT,
                popularity DOUBLE PRECISION,
                poster_path TEXT,
                tagline TEXT,
                genres TEXT,
                production_companies TEXT,
                production_countries TEXT,
                spoken_languages TEXT,
                keywords TEXT
            );
        """)
        logging.info("table created")
        conn.commit()
        cur.close()

    def insert_data(self):
        logging.info("inserting data")
        df = pd.read_parquet(f"{Path(__file__).parent.parent.parent}/data/silver/movies.parquet")
        df = df.where(pd.notnull(df), None)
        df = df.replace({np.nan: None})
        df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
        df['release_date'] = df['release_date'].where(df['release_date'].notna(), None)
        df = df.astype(object).where(pd.notna(df), None)
        conn = self.connect_to_database()

        with conn.cursor() as cur:
            with cur.copy("""
                    COPY tmdb.movies (
                        movie_id, title, vote_average, vote_count, status, release_date,
                        revenue, runtime, adult, backdrop_path, budget, homepage,
                        imdb_id, original_language, original_title, overview,
                        popularity, poster_path, tagline, genres,
                        production_companies, production_countries,
                        spoken_languages, keywords
                    )
                    FROM STDIN
                """) as copy:
                for row in df.itertuples(index=False, name=None):
                    copy.write_row(row)

        conn.commit()


        # for index, row in df.iterrows():
        #     print(row['title'], row['genres'], row['production_companies'], row['production_countries'], row['spoken_languages'], row['keywords'])
        #     try:
        #         cur.execute("""
        #             INSERT INTO tmdb.movies (id, title, vote_average, vote_count, status, release_date, revenue, runtime, adult, backdrop_path, budget, homepage, imdb_id, original_language, original_title, overview, popularity, poster_path, tagline, genres, production_companies, production_countries, spoken_languages, keywords)
        #             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s );
        #         """, (row['id'], row['title'], row['vote_average'], row['vote_count'], row['status'], row['release_date'], row['revenue'], row['runtime'], row['adult'], row['backdrop_path'], row['budget'], row['homepage'], row['imdb_id'], row['original_language'], row['original_title'], row['overview'], row['popularity'], row['poster_path'], row['tagline'], row['genres'], row['production_companies'], row['production_countries'], row['spoken_languages'], row['keywords']))
        #
        #     except Exception as e:
        #         logging.error(f"REAL ERROR: {e}")
        #         logging.error(f"ROW: {row}")
        #         conn.rollback()
        #         continue
        #
        # conn.commit()
        # cur.close()

        logging.info("data inserted")

    def main(self):
        logging.info("starting gold layer")

        self.create_schema()
        self.create_table()
        self.insert_data()

        logging.info("gold layer finished")