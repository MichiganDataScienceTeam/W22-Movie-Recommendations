import pandas as pd
import numpy as np

N = 10 # 10 recs
class Filter:
    def __init__(self, data_csv='data4_02.csv'):  
        self.df_filters = pd.read_csv(f'data/{data_csv}')


    def all_filters(self, recommendations, movies, filters): # (df, list[movie id's], dict)
        recommendations = self.drop_movies(recommendations, movies)
        recommendations = self.drop_year(recommendations, filters)
        recommendations = self.drop_genres(recommendations, filters)
        # recommendations = self.drop_audience(recommendations, filters)
        recommendations = self.drop_runtime(recommendations, filters)

        # print(recommendations['movie'][:N].to_list()

        return recommendations['movie'][:N].to_list()

    def drop_movies(self, recommendations, movies):
        return recommendations[recommendations.movie.isin(movies) == False]


    def drop_year(self, recommendations, filters):  # need two year filters, <= and >=

        before = filters['year'][1]
        after = filters['year'][0]
        validyears = self.df_filters[(self.df_filters['year'] <= before) & (self.df_filters['year'] >= after)]
        recommendations = recommendations[recommendations['movie'].isin(list(validyears['cleaned_mov_id'].values)) == True]
        return recommendations


    def drop_genres(self, recommendations, filters): # maybe poor name bc its filtering not dropping
        if filters['genre'][0] != 'Genre_No Filter':
            fil = self.df_filters[self.df_filters[filters['genre'][0]]== True]
            recommendations = recommendations[recommendations.movie.isin(list(fil['cleaned_mov_id'].values)) == True]

        if filters['genre'][1] != 'Genre_No Filter':
            fil = self.df_filters[self.df_filters[filters['genre'][1]]== False]
            recommendations = recommendations[recommendations.movie.isin(list(fil['cleaned_mov_id'].values)) == True]
        return recommendations


    def drop_audience(self, recommendations, filters):
        #  not being done now...
        return recommendations


    def drop_runtime(self, recommendations, filters):
        before = filters['runtime'][1]
        after = filters['runtime'][0]
    
        validyears = self.df_filters[(self.df_filters['runtime'] <= before) & (self.df_filters['runtime'] >= after)]
        recommendations = recommendations[recommendations['movie'].isin(list(validyears['cleaned_mov_id'].values)) == True]
        return recommendations