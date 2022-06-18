import streamlit as st
    

def intro():
    st.set_page_config('MDST Movie Recs', 'https://avatars.githubusercontent.com/u/15266139?s=200&v=4')
    st.title('Movie Recommendations')
    st.image('./icons/front_page_movies.png')
    st.markdown('**Project Leads:** _Justin Paul, Sachchit Kunichetty_')
    st.markdown('**Team Members:** (in alphabetical order by first name) _Charlie Tran, Danny Colleran, \
                Griffin Olson-Allen, Hanh Nguyen, Josh Zhang, Justin Xiao, Kaixin Zhao, Kyle Hoffmeyer, \
                    Rohan Gupta, Steve Fan, Ting-Ting Kao_')
    st.markdown('**Project Repository:** https://github.com/MichiganDataScienceTeam/movie-recommendations ')

    st.subheader('Rationale')
    st.markdown("Let's set the scene: you're an avid fan of superhero movies and drama films. \
        You've already watched every _Avengers_ movie and also _Inception,_ those being some of your favorite movies. \
            The next day, your favorite streaming service recommends you watch _The Dark Knight_ - and you love it! \
                It's the perfect combination of superhero action and drama that you craved.")
    st.markdown("Let's take a step back though - how did the streaming service know you would like _The Dark Knight?_ \
        Additionally, how can we create software to automatically perform such recommendations?")

    st.subheader('Methods')
    st.markdown("In its fundamental components, recommending movies involves")
    st.markdown("1. Understanding user preferences for _all_ movies - for example, a 1-5 star rating for each movie")
    st.markdown("2. Choosing the movies that the user most prefers - for example, recommending movies that the user have given 5 stars")
    st.markdown("This will always produce the best recommendations - if the user would give a movie 5 stars, they will certainly enjoy watching that movie.")
    st.markdown("However, streaming services don't have access to user preferences for all movies - users have only watched a small subset of all movies, \
        and so it becomes impossible to choose the movies that the user would like the most.")
    st.markdown("This is where data science comes into play - by studying movie rating data and analyzing trends in how other users watch movies, \
        we could guess the ratings that a user will give movies, and then recommend movies which the user is predicted to give the highest rating to. \
            This method of recommendation is called **Collaborative Filtering.**")
    st.markdown("To make these guesses, we studied two fundamental types of collaborative filtering approaches: a **Nearest Neighbor** approach and a **Latent Factor** approach.")

    st.image('https://avatars.githubusercontent.com/u/15266139?s=200&v=4')
    
if __name__ == '__main__':
    intro()