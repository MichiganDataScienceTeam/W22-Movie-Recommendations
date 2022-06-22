import pathlib
import streamlit as st
import os, sys, pathlib
import pandas as pd

@st.cache
def readData():
    p = pathlib.Path.cwd()
    data = p / 'data'
    featuresDF = pd.read_csv(data / 'data4_02.csv')
    urMatrixDF = pd.read_csv(data / 'user_rating_matrix.csv', index_col=0)
    urMatrixDF.columns.name = urMatrixDF.index.name
    urMatrixDF.index.name = 'title'

    return featuresDF, urMatrixDF

def dataset():
    # st.set_page_config('Dataset', 'https://avatars.githubusercontent.com/u/15266139?s=200&v=4')
    st.title("Datasets")
    fDF, urDF = readData()

    st.caption("Features Dataset *")
    st.dataframe(fDF)
    
    st.text('')
    st.text('')

    st.caption("User Ratings of Movies 0 means unwatched")
    st.dataframe(urDF)
    
    st.subheader('Sources')
    st.markdown("*'year' through 'imdbId' were scraped from https://www.imdb.com/")
    st.markdown("Both datasets used data from https://grouplens.org/datasets/movielens/")

    st.image('https://avatars.githubusercontent.com/u/15266139?s=200&v=4')

