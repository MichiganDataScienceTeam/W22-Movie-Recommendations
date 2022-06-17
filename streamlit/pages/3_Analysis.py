import streamlit as st

st.set_page_config('Analysis', 'https://avatars.githubusercontent.com/u/15266139?s=200&v=4')
st.title('Analysis')

st.header("EDA (Exploratory Data Analysis)")

col1, col2 = st.columns(2)

col1.image("./icons/eda_genres.jpg")
col1.caption("Number of movies tagged with each genre")

col2.image("./icons/eda_rating_frequencies.jpg")
col2.caption("Histogram of rating frequencies")


#NEAREST NEIGHBORS
st.header("Nearest Neighbors")
st.markdown("Below are some sample movie suggestions")
col1, col2, col3 = st.columns(3)
col1.image("./icons/nn_iron_man.jpg")
col2.image("./icons/nn_forrest_gump.jpg")
col3.image("./icons/nn_avatar.jpg")
st.markdown("For these popular movies, it recommends pretty similar content. For example, it recommended Marvel movies for someone who likes _Iron Man._")

col1, col2 = st.columns(2)
col1.image("./icons/nn_8_seconds.jpg")
col2.image("./icons/nn_8_seconds_list.jpg")
st.markdown("Less popular movies are harder to predict. One difficulty with dealing with the long-tail problem is that the actual vectors representing \
            each movie can realistically be the same as is the case for _8 Seconds._ \
                This is a particularly large limitation for the nearest neighbors algorithm we implemented.")

#LATENT FACTORS
st.header("Latent Factor")
st.markdown("The Asymmetric SVD latent factor algorithm makes realistic predictions, but struggles with certain genres.")
st.caption("Random user #1")
col1, col2 = st.columns(2)

col1.image("./icons/latent_factor_1a.jpg")
col1.caption("Most highly rated movies for user 1")
col2.image("./icons/latent_factor_1b.jpg")
col2.caption("Movies with highest predicted ratings for the user 1")

st.markdown("Consider the example above. This user rates crime and drama movies such as _Goodfellas (1990)_ and _The Godfather (1972)_ highly. \
    As a result, it should be expected that this user wants to watch more crime and drama movies. \
        Indeed, the latent factor approach predicts predominantly crime and drama movies to have the highest ratings such as _Fight Club (1999)_ and _Reservoir Dogs (1992)._")
st.markdown("This model fails in that it tends to give more popular movies a greater rating such as _Forrest Gump (1994),_ even though in terms of genre it is only loosely related to crime and genre. \
    In other instances when a user highly rates movies from less popular genres like romance, this problem is exacerbated and the model tends to predict popular movies that do not correspond at all to the genre, as seen below.")

st.caption("Random user #2")
col1, col2 = st.columns(2)

col1.image("./icons/latent_factor_2a.jpg")
col1.caption("Most highly rated movies for user 2. Most of the movies here are romance and comedy movies.")
col2.image("./icons/latent_factor_2b.jpg")
col2.caption("Movies with highest predicted ratings for the user 2. Notice that very few of the movies recommended are romance and comedy movies. This is a fault of our model.")

st.image('https://avatars.githubusercontent.com/u/15266139?s=200&v=4')