""" streamlit app for expression analysis """


# libraries

import streamlit as st
import pandas as pd
import polars as pl
import plotly.express as px
# import matplotlib.pyplot as plt

import duckdb


file_paquet = "/home/ec2-user/projects/omics_analysis/scripts/file_tpm_pheno_gene_pqt.parquet"
# query
# query = """
#         SELECT tpm, gene, _study, _primary_site
#         FROM parquet_scan('{}')
#         WHERE gene = 'STT3A' AND _study = 'GTEX'
#         """.format(file_paquet)

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

    @staticmethod
    def create_gene_study_query(geneid: str, studyid: str, file_paquet: str):
        """ create query to get data from parquet file """
        query = """
                SELECT tpm,
                        gene, 
                        _study, 
                        _primary_site AS primary_site, 
                        detailed_category, 
                        'primary disease or tissue' AS primary_disease_or_tissue
                FROM parquet_scan('{}')
                WHERE gene = '{}' AND _study = '{}'
                """.format(file_paquet, geneid, studyid)
        return query

    def get_data(self, geneid: str, studyid: str = 'GTEX') -> pd.DataFrame:
        """ get data from parquet file using duckdb """
        query = queryDuckDB.create_gene_study_query(
            geneid=geneid, studyid=studyid, file_paquet=self.file_parquet)
        return self.conn.execute(query).fetchdf()


# function to render streamlit app


def render_app(df):
    """ render streamlit app """
    st.title("Expression analysis")
    st.write("This is a streamlit app for expression analysis")
    st.table(df.head(10))
    # Create the box plot using Plotly Express
    fig = px.box(df, x="primary_site",
                 y="tpm", color="primary_site")
    # Rotate x-axis labels by 90 degrees
    fig.update_xaxes(tickangle=90)
    # Display the box plot using Streamlit
    st.plotly_chart(fig)
    # st.plotly_chart(fig)


# main
def main():
    """ main function """
    # create an instance of the class
    query_duckdb = queryDuckDB(file_paquet)
    # get data from parquet file using duckdb
    df = query_duckdb.get_data(
        geneid='EGFR',
        studyid='TCGA'
    )
    print(df.head(10))
    # show data
    render_app(df.head(10))


if __name__ == "__main__":
    main()
