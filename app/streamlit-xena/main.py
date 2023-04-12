"""streamlit app to display the omics data"""

# import libraries
import streamlit as st
import pandas as pd
import duckdb

# load data

# create database


# build the app
headerSection = st.container()
mainSection = st.container()
leftNav = st.sidebar


# header
with headerSection:
    st.title("Omics Data")
    st.write("This is a streamlit app to display the omics data")

# main
with mainSection:
    st.write("This is the main section")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Left Column")
        st.write("This is the left column")
        textValue = st.text_input("Gene symbol", "")
        st.write("You typed:", textValue)

    with right_column:
        st.header("Right Column")
        st.write("This is the right column")

# left nav
with leftNav:
    st.write("This is the menu")
    st.button("Button", on_click=lambda: st.write("Button clicked!"))


def omics_main():
    pass


if __name__ == "__main__":
    omics_main()
