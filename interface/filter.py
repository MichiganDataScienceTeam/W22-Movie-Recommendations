import pandas as pd
import numpy as np

N = 10 # 10 recs
class Filter:
    def __init__(self):  
        pass


    def all_filters(self, recommendations, movies, filters): # (df, list[movie id's], dict)
        recommendations = self.drop_movies(recommendations, movies)
        recommendations = self.drop_year(recommendations, filters)
        recommendations = self.drop_genres(recommendations, filters)

        # print(recommendations['movie'][:N].to_list())
        return recommendations['movie'][:N].to_list()

    def drop_movies(self, recommendations, movies):
        return recommendations[recommendations.movie.isin(movies) == False]


    def drop_year(self, recommendations, filters):  # need two year filters, <= and >=
        return recommendations


    def drop_genres(self, recommendations, filters): # maybe poor name bc its filtering not dropping
        return recommendations