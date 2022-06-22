import streamlit as st


def methods():
    # st.set_page_config('Methods', 'https://avatars.githubusercontent.com/u/15266139?s=200&v=4')
    st.title('Methods')

    #NEAREST NEIGHBORS
    st.header('Nearest Neighbors')

    st.markdown("**Key:** Users that have similar ratings patterns for the movies they have watched are likely to rate all other movies similarly. \
        Use this relationship to guess the rating that a user would give for some movie.")

    st.markdown("For example, let us consider the case of Alice, Bob, and Carl")
    st.markdown("- Alice rated _The Lord of the Rings_ as 5 stars and Carl rated The _Lord of the Rings_ as 2 stars. \
        It seems that Carl and Alice generally rate opposingly to each other. If Alice rates _The Godfather_ as 1 star, \
            we might predict that Carl rates _The Godfather_ as 4 stars.")
    st.markdown("- Bob rated _Jurassic Park_ as 1 star and Carl rated _Jurassic Park_ as 2 stars. It seems Bob and Carl tend to generally rate movies similarly. \
        If Bob rates _The Godfather_ as 5 stars, then we might predict that Carl rates _The Godfather_ as 4 stars.")

    st.subheader('Recommending Movies')
    st.markdown("The relationship between movies and the associated ratings from each user can be represented in 610-D space (for each user). Then recommended movies are taken by comparing which movie vectors are closest to the ones that the user enjoyed. This can be done either by euclidean distance (which was used) or by angular distance (the cosine between the vectors). \
        The movies with the smallest distance to the targeted movie is the one most similar from using nearest neighbors.")

    st.subheader('Limitations')
    st.markdown("A major limitation of this method is that the dataset is sparse. \
        There are multiple movies that either have no ratings or the exact same ratings (over 610 users) as other movies. \
            If every movie was rated this would be a good thing and would make recommendations fairly obvious and easier to justify. \
                However, as movies that users did not rate were simply given a rating of 0.0, this introduces unpredictability in recommending unpopular movies.")

    st.markdown("Another limitation was the inability to use content-based features (such as the genre, cast, or director) for movie recommendations. \
        This was tested for predicting movie ratings and only achieved an accuracy of around 20%. \
        There was not enough time to continue a content-based model nor enough time to fully incorporate some features into filtering for the final application. ")

    st.subheader('Improvements')
    st.markdown("For future use with this dataset, we believe that using word2vec in order to utilize the comments people gave for movies could be very helpful. \
        Additionally, making use of a larger, less dense dataset would be useful to avoid general issues stemming from the long-tail problem.")

    #LATENT FACTORS
    st.header('Latent Factor')
    st.markdown("**Key:** To predict ratings, learn some underlying latent factors that describe both users and movies, and match users to movies by comparing these factors. \
        The strength of this match forms the rating for that user.")
    st.markdown("Latent factors are intuitively underlying properties that can describe both movies and users in the data. \
        In this case, if some user/movie falls has some latent factor, the latent factor has a greater magnitude.")

    st.subheader('Asymmetric Singular Value Decomposition')
    st.markdown("With the notion of latent factors, the task of predicting movie ratings can be rewritten as the following: \
        _learn latent factors for movies and users so that the dot product of the user latent vector and the movie \
            latent vector gives the rating that the user would give that movie._")
    st.markdown("Mathematically, this can be described as learning matrices _Z, V_ \
        that multiply with the utility matrix _R_ to produce the predicted rating matrix as below:")
    st.image('./icons/matrix_info.jpg')

    st.markdown("This is the Asymmetric SVD formula for producing the utility matrix with all filled ratings with _n_ users and _m_ movies. Some important notes: ")
    st.markdown("- _?_ values in the R matrix are the missing ratings that we would like to fill in")

    st.markdown("- The vectors _z_ in the second matrix are vectors describing how the user latent factors relate to the rating matrix. \
        To get the user latent vectors, compute _Rz_")
    st.markdown("- The vectors _v_ in the third matrix are the latent vectors for each movie")
    st.markdown("This formulation, called **asymmetric singular value decomposition** differs from the standard latent factor approach \
        to make the recommendation system model-based (independent of the number of users).")

    st.subheader("Training")

    col1, col2 = st.columns(2)
    col1.markdown("To learn _Z_ and _V_ , we train on reconstructing the utility matrix from before using Stochastic Gradient Descent (in practice we trained using the _Adam_ optimizer). \
        Batches are chosen randomly by selecting a random subset of users in the utility matrix for which ratings are reconstructed. \
            The first 500 users form the training set, and the last 110 users form the testing set.")
    col1.markdown("Training Settings:")
    col1.markdown("- Latent Factors - 100")
    col1.markdown("- Loss - Mean Squared Error")
    col1.markdown("- Optimizer - AdamW w/ Weight Decay = 0.001")
    col1.markdown("- Learning Rate - 0.0001")
    col1.markdown("- Epochs = 10000")
    col1.markdown("- Batch Size = 128")
    col1.markdown("a loss of 0.2 was reached on the test set, indicating that on average the predicted rating (in the range 0.5-5 stars) \
        varied from the actual rating by 0.45 stars.")

    col2.image('./icons/training_data.jpg')
    col2.caption("Loss curves on the training and testing set. The final testing set loss was about 0.2, \
        indicating on average the predicted rating varied from the true rating by 0.44 stars. \
        This indicates that our model has generally strong performance in predicted the correct rating.")

    st.image('https://avatars.githubusercontent.com/u/15266139?s=200&v=4')