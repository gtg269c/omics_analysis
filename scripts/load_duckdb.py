"""
script to load data into duckdb
"""

import pandas
import duckdb

# Specify the Parquet file path and the size of each chunk to read
parquet_file = '/mnt/d/Research/Omics/Xena/data/file_tpm_pheno_gene_pqt.parquet'
database_name = '/mnt/d/Research/Omics/Xena/data/TcgaTargetGtex_xena.duckdb'

# class to connect, access duckdb database


class DuckDB:
    def __init__(self, database_name):
        self.database_name = database_name
        self.conn = duckdb.connect(database=database_name, read_only=False)

    @staticmethod
    def create_table_query(file_parquet: str, studyid: str):
        query_load_study = f"""
                            CREATE OR REPLACE TABLE {studyid.lower()}_table
                            AS SELECT tpm, gene, _study, _primary_site
                            FROM parquet_scan('{file_parquet}')
                            WHERE _study = '{studyid}'
                            """
        return query_load_study

    def create_table(self, file_parquet: str, studyid: str):
        query = DuckDB.create_table_query(file_parquet, studyid)
        self.conn.execute(query)

    def close(self):
        self.conn.close()


# create duckdb database and load data from parquet
def create_database(database_name: str, parquet_file: str, studyid: str):
    # create duckdb database table for each study
    for study in studyid:
        print(f"Loading {study} data into duckdb database")
        duckdb_obj = DuckDB(database_name)
        duckdb_obj.create_table(parquet_file, study)
        duckdb_obj.close()
        print(f"Finished loading {study} data into duckdb database")


# main function
if __name__ == "__main__":
    list_studies = ['GTEX', 'TCGA', 'TARGET']
    create_database(database_name, parquet_file, list_studies)
