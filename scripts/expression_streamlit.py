""" streamlit app for expression analysis """


# libraries

import streamlit as st
import pandas as pd
import polars as pl
import plotly.express as px
# import matplotlib.pyplot as plt

import duckdb


# file_paquet = "/home/ec2-user/projects/omics_analysis/scripts/file_tpm_pheno_gene_pqt.parquet"
file_duckdb = "/mnt/d/Research/Omics/Xena/data/TcgaTargetGtex_xena.duckdb"

# create a class to read data from parquet file using duckdb


class queryDuckDB:
    def __init__(self, file_db):
        self.file_db = file_db
        self.conn = duckdb.connect(database=self.file_db, read_only=False)

    @staticmethod
    def create_gene_study_query(geneid: str, studyid: str):
        """ create query to get data from duckdb table"""
        query = """
                SELECT tpm,
                        gene, 
                        _study, 
                        _primary_site AS primary_site, 
                FROM {}_table
                WHERE gene = '{}' AND _study = '{}'
                """.format(studyid.lower(), geneid, studyid)
        return query

    def get_data(self, geneid: str, studyid: str = 'GTEX') -> pd.DataFrame:
        """ get data from parquet file using duckdb """
        query = queryDuckDB.create_gene_study_query(
            geneid=geneid, studyid=studyid)
        return self.conn.execute(query).fetchdf()


# function to load data from duckdb
def load_data(file_db, geneid, studyid):
    # create an instance of the class
    query_duckdb = queryDuckDB(file_db)
    # get data from parquet file using duckdb
    df = query_duckdb.get_data(
        geneid=geneid,
        studyid=studyid
    )
    return df


# App
def app():
    # title
    st.title("Expression analysis")
    st.write("This is a streamlit app for expression analysis")

    # get user input
    if st.sidebar:
        geneid = st.sidebar.text_input("Gene ID", "EGFR")
        studyid = st.sidebar.multiselect(
            "Study ID", ["TCGA", "GTEX", "TARGET"])
        submitted = st.sidebar.button("Submit")

    # load data
    if submitted:
        print(f"Type of geneid: {type(geneid)}")
        print(f"Type of studyid: {type(studyid)}")
        df = load_data(file_duckdb, geneid, studyid[0])

        # check if data is empty
        if df.empty:
            st.write("No data found")
        else:
            # show data
            st.table(df.head(10))
            # Create the box plot using Plotly Express
            fig = px.box(df, x="primary_site",
                         y="tpm", color="primary_site")
            # Rotate x-axis labels by 90 degrees
            fig.update_xaxes(tickangle=90)
            # Set the title as geneid
            fig.update_layout(title_text=df['gene'][0] +
                              " expression in "+df['_study'][0]+" study")

            # Display the box plot using Streamlit
            st.plotly_chart(fig)
            # st.plotly_chart(fig)


if __name__ == "__main__":
    app()
