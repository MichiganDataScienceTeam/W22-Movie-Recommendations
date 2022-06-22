import streamlit as st
import pandas as pd

def analysis():
    # st.set_page_config('Analysis', 'https://avatars.githubusercontent.com/u/15266139?s=200&v=4')
    st.title('Analysis')

    st.header("EDA (Exploratory Data Analysis)")

    col1, col2 = st.columns(2)

    col1.image("./icons/eda_genres.jpg")
    col1.caption("Number of movies tagged with each genre")

    col2.image("./icons/eda_rating_frequencies.jpg")
    col2.caption("Histogram of rating frequencies")


    #NEAREST NEIGHBORS
    st.header("Nearest Neighbors")
    st.caption("Top 10 movie recommendations for _Forrest Gump,_ _Iron Man,_ and _Avatar._")

    dfKNN = pd.DataFrame({"Forrest Gump (1994)":["Jurassic Park (1993)", "The Shawshank Redemption (1994)", "Apollo 13 (1995)", "Pulp Fiction (1994)", "Braveheart (1995)", \
        "Mrs. Doubtfire (1993)", "The Lion King (1994)", "Speed (1994)", "The Silence of the Lambs (1991)", "Terminator 2: Judgement Day (1991)"],\
    "Iron Man (2008)":["Iron Man 2 (2010)", "The Avengers (2012)", "Thor (2011)", "Iron Man 3 (2013)", "Watchmen (2009)", "X-Men: First Class (2011)", \
        "Kung Fu Panda (2008)", "Star Trek (2009)", "Pirates of the Caribbean: At World's End (2007)", "Guardians of the Galaxy (2014)"],
    "Avatar (2009)": ["Kung Fu Panda (2008)", "District 9 (2009)", "The Hangover (2009)", "Harry Potter and the Half-Blood Prince (2009)", "I Am Legend (2007)", \
        "Sherlock Holmes (2009)", "Thor (2011)", "X-Men Origins: Wolverine (2009)", "Zombieland (2009)", "Iron Man 2 (2010)"]})
    dfKNN.index += 1
    st.dataframe(dfKNN)
    st.markdown("For these popular movies, it recommends similar content. For example, it recommended Marvel movies for someone who likes _Iron Man._")

    col1, col2 = st.columns(2)

    sec8 = pd.DataFrame({"8 Seconds (1994)": ["Johnny Be Good (1988)", "The Serpent and the Rainbow (1988)", "American Ninja (1985)", "Bright Lights, Big City (1988)", "Blue Chips (1994)", \
        "Navy Seals (1990)", "Next of Kin (1989)", "Get Carter (2000)", "The Distinguished Gentleman (1992)", "Being Human (1993)"],\
            "Movie ID": ["140", "4598", "7515", "425", "1384", "1207", "6026", "6080", "2424", "3387"],\
                "Distance": ["0.000000", "0.000000", "1.000000", "2.236068", "2.692582", "2.872281", "3.162278", "3.201562", "3.605551", "3.500000"]})
    sec8.index += 1

    st.caption("Top 10 movie recommendations for _8 Seconds_ and their corresponding IDs and distances (in euclidean space)")
    st.dataframe(sec8)
    st.markdown("Less popular movies are harder to predict. One difficulty with dealing with the long-tail problem is that the actual vectors representing \
                each movie can realistically be the same. For example, _8 Seconds,_ _Johnny Be Good,_ and _The Serpent and the Rainbow_ have the same ratings. \
                    This is a particularly large limitation for the nearest neighbors algorithm we implemented.")

    #LATENT FACTORS
    st.header("Latent Factor")
    st.markdown("The Asymmetric SVD latent factor algorithm makes realistic predictions, but struggles with certain genres.")
    st.subheader("Random User #1")
    col1, col2 = st.columns(2)


    df1a = pd.DataFrame({"Movies": ["The Sandlot (1993)", "City of God (Cidade de Deus) (2002)", "Blow (2001)", "True Romance (1993)", "Raging Bull (1980)", \
            "Goodfellas (1990)", "61* (2001)", "The Godfather (1972)", "American Gangster (2007)", "Casino (1995)"],\
        "Genres": ["Children | Comedy | Drama", "Action | Adventure | Crime | Drama | Thriller", "Crime | Drama", "Crime | Thriller", "Drama",\
            "Crime | Drama", "Drama", "Crime | Drama", "Crime | Drama | Thriller", "Crime | Drama"]})
    df1a.index += 1

    df1b = pd.DataFrame({"Movies": ["Fight Club (1999)", "Pulp Fiction (1994)", "The Shawshank Redemption (1994)", "The Usual Suspects (1995)", \
            "Reservoir Dogs (1992)", "The Departed (2006)", "The Matrix (1999)", "Goodfellas (1990)", "Forrest Gump (1994)", "Inception (2010)"],\
        "Genres": ["Action | Crime | Drama | Thriller", "Comedy | Crime | Drama | Thriller", "Crime | Drama", "Crime | Mystery | Thriller", \
            "Crime | Mystery | Thriller", "Crime | Drama | Thriller", "Action | Sci-Fi | Thriller", "Crime | Drama", "Comedy | Drama | Romance | War", \
            "Action | Crime | Drama | Mystery | Sci-Fi | Thriller"]})
    df1b.index += 1



    col1.caption("User's most highly rated movies")
    col1.dataframe(df1a)
    col2.caption("Model's top predictions")
    col2.dataframe(df1b)

    st.markdown("Consider the example above. This user rates crime and drama movies such as _Goodfellas (1990)_ and _The Godfather (1972)_ highly. \
        As a result, it should be expected that this user wants to watch more crime and drama movies. \
            Indeed, the latent factor approach predicts predominantly crime and drama movies to have the highest ratings such as _Fight Club (1999)_ and _Reservoir Dogs (1992)._")
    st.markdown("This model fails in that it tends to give more popular movies a greater rating such as _Forrest Gump (1994),_ even though in terms of genre it is only loosely related to crime and genre. \
        In other instances when a user highly rates movies from less popular genres like romance, this problem is exacerbated and the model tends to predict popular movies that do not correspond at all to the genre, as seen below.")

    st.subheader("Random User #2")
    col1, col2 = st.columns(2)


    df2a = pd.DataFrame({"Movies": ["The Shawshank Redemption (1994)", "Office Space (1999)", "Singin' in the Rain (1952)", "Mr. & Mrs. Smith (2005)", "Juno (2007)", "Easy A (2010)", \
            "The Royal Tenenbaums (2001)", "Monty Python and the Holy Grail (1975)", "I Heart Huckabees (2004)", "Moonrise Kingdom (2012)"],\
        "Genres": ["Crime | Drama", "Comedy | Crime", "Comedy | Musical | Romance", "Action | Adventure | Comedy | Romance", "Comedy | Drama | Romance", "Comedy | Romance", \
            "Comedy | Drama", "Adventure | Comedy | Fantasy", "Comedy", "Comedy | Drama | Romance"]}) 
    df2a.index += 1

    df2b = pd.DataFrame({"Movies": ["The Matrix (1999)", "The Shawshank Redemption (1994)", "The Incredibles (2004)", "Pirates of the Caribbean: The Curse of the Black Pearl (2003)", \
            "Forrest Fump (1994)", "Pretty Woman (1990)", "Star Wars: Episode VI - The Return of the Jedi (1983)", "The Bourne Identity (2002)", "Finding Nemo (2003)", "Star Wars: Episode IV - A New Hope"],\
        "Genres": ["Action | Sci-Fi | Thriller", "Crime | Drama", "Action | Adventure | Animation | Children | Comedy", "Action | Adventure | Comedy | Fantasy", "Comedy | Drama | Romance | War",\
            "Comedy | Romance", "Action | Adventure | Sci-Fi", "Action | Mystery | Thriller", "Adventure | Animation | Children | Comedy", "Action | Adventure | Sci-Fi"]})
    df2b.index += 1

    col1.caption("User's most highly rated movies. Most are romance and comedies.")
    col1.dataframe(df2a)
    col2.caption("Model's top predictions. Note that few are romance and comedies. This is a fault of our model.")
    col2.dataframe(df2b)

    st.image('https://avatars.githubusercontent.com/u/15266139?s=200&v=4')