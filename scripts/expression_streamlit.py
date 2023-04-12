""" streamlit app for expression analysis """


## libraries

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import duckdb


file_paquet = "scripts/file_tpm_pheno_gene_pqt.parquet"

## functions

def get_data(input_parquet: str, query: str) -> pd.DataFrame:
    """ get data from parquet file using duckdb """
    pass
