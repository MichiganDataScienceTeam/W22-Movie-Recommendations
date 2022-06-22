import streamlit as st
import os, sys
import pandas as pd

p = os.path.abspath('.')
sys.path.insert(1, p)
from interface import models

st.set_page_config('UI', 'https://avatars.githubusercontent.com/u/15266139?s=200&v=4')

@st.cache(allow_output_mutation=True)
def loadModels():
    return models.KNN_COLLAB('no pkl', 'no_csv'), models.MatrixFactorizationModel('./data/torchsvd.pt')
    
KNN, MF = loadModels()

MOVIE_ID = [7396, 5756, 2640]  # important that it is from csv matrix
FILTERS = {
    'genre': ['Genre_No Filter', 'Genre_No Filter'],
    'year': [1970, 2020],
    'runtime': [0, 300],
}

def filterHelper(string):
   return f'Genre_{string}'

def dfRecommendation():
    knn_list = KNN.recommend(MOVIE_ID, FILTERS)
    mf_list = MF.recommend(MOVIE_ID, FILTERS)

    knn_df = pd.DataFrame({"Movies": knn_list})
    knn_df.index += 1
    mf_df = pd.DataFrame({"Movies": mf_list})
    mf_df.index += 1
    return knn_df, mf_df

#QUIZ
st.title('Quiz')
#Question 1
q1 = {  # title: movie id (but really a dict...)
            'Saw': 7396,
            'Star Wars: Episode IV - A New Hope': 8001,
            'The Lion King': 5103,
            'The Notebook': 6188,
        }


# QUESTION 2 
q2 = {
    'Moneyball': 5756,
    'Shawshank Redemption': 7593,
    'Ted': 8337,
    'The Dark Knight': 2163,
}


# QUESTION 3
q3 = {
    'Eagle Eye': 2640,
    'Elf': 2700,
    'Interstellar': 4396,
    'Richie Rich': 7127
}

genres = [
    "No Filter",
    "Action",
    "Adventure",
    "Animation",
    "Children's",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Fantasy",
    "Film-Noir",
    "Horror",
    "Musical",
    "Mystery",
    "Romance",
    "Sci-Fi",
    "Thriller",
    "War",
    "Western"
]

years =[1970, 1980, 1990, 2000, 2010, 2020]
rtimes =[0, 60, 75, 90, 105, 120, 135, 150, 165, 180, 300]

st.markdown("Pick your favorite movie in each of the selection boxes")
col1, col2, col3 = st.columns(3)
MOVIE_ID[0] = q1[col1.selectbox("Q1", sorted(q1.keys()))]
MOVIE_ID[1] = q2[col2.selectbox("Q2", sorted(q2.keys()))]
MOVIE_ID[2] = q3[col3.selectbox("Q3", sorted(q3.keys()))]

#FILTER
st.header('Filter Movies')
st.markdown("Add filters to the recommender")

col1, col2 = st.columns(2)
FILTERS['genre'][0] = filterHelper(col1.selectbox("Required Genre", genres))
FILTERS['genre'][1] = filterHelper(col2.selectbox("Exclude Genre", genres))

FILTERS['year'][0] = col1.selectbox("Start Year", years)
FILTERS['year'][1] =col2.selectbox("End Year", years[::-1])

FILTERS['runtime'][0] = col1.selectbox("Minimum Runtime", rtimes)
FILTERS['runtime'][1] = col2.selectbox("Maximum Runtime", rtimes[::-1])

#RESULTS
st.header("Results")
col1, col2 = st.columns(2)

KNN_DF, MF_DF = dfRecommendation()

col1.subheader("Nearest Neighbors")
col1.dataframe(KNN_DF)
col2.subheader("Matrix Factorization")
col2.dataframe(MF_DF)





st.image('https://avatars.githubusercontent.com/u/15266139?s=200&v=4')


# def updateMovID()

