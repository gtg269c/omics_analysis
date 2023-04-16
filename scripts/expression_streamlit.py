""" streamlit app for expression analysis """


# libraries

import streamlit as st
import pandas as pd
import polars as pl
import plotly.express as px
# import matplotlib.pyplot as plt

import duckdb


file_paquet = "/mnt/d/Research/Omics/Xena/data/file_tpm_pheno_gene_pqt.parquet"
# query
query = """
        SELECT tpm, gene, _study, _primary_site
        FROM parquet_scan('{}')
        WHERE gene = 'STT3A' AND _study = 'GTEX'
        """.format(file_paquet)

# query = """
#         SELECT *
#         FROM parquet_scan('{}')
#         LIMIT 10
#         """.format(file_paquet)

# functions

# create a class to read data from parquet file using duckdb


class queryDuckDB:
    def __init__(self, file_parquet):
        self.file_parquet = file_parquet
        self.conn = duckdb.connect(database=':memory:', read_only=False)
    #     self.conn.execute(
    #         'CREATE OR REPLACE TABLE stt3a_gtex_table (tpm FLOAT, gene STRING, _study STRING, _primary_site STRING)')
    #     self.load_data()

    # def load_data(self):
    #     """ load data from parquet file into duckdb """
    #     with pq.ParquetFile(self.file_parquet) as pf:
    #         for i in range(pf.num_row_groups):
    #             start = i * chunk_size
    #             end = min(start + chunk_size, pf.metadata.num_rows)
    #             table = pf.read(columns=['tpm', 'gene', '_study',
    #                                      '_primary_site'], row_group=i, start=start, stop=end)
    #             rows = [tuple(row) for row in table]
    #             query = f"INSERT INTO stt3a_gtex_table VALUES {','.join(['(?,?,?,?)']*len(rows))}"
    #             self.conn.execute(query, rows)

    def get_data(self, query):
        """ get data from parquet file using duckdb """
        return self.conn.execute(query).fetchdf()

# function to render streamlit app


def render_app(df):
    """ render streamlit app """
    st.title("Expression analysis")
    st.write("This is a streamlit app for expression analysis")
    st.table(df.head(10))
    # Create the box plot using Plotly Express
    fig = px.box(df, x="_primary_site", y="tpm", color="_primary_site")
    # Display the box plot using Streamlit
    st.plotly_chart(fig)
    # st.plotly_chart(fig)


# main
def main():
    """ main function """
    # create an instance of the class
    query_duckdb = queryDuckDB(file_paquet)
    # get data from parquet file using duckdb
    df = query_duckdb.get_data(query)
    print(df.head(10))
    # show data
    render_app(df.head(10))


if __name__ == "__main__":
    main()
