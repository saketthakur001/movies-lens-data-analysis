import imdb

# Create an IMDb access object
ia = imdb.IMDb()

import pandas as pd
new_df = pd.read_csv("new_df.csv")

# all the that has more than 200 count
new_df = new_df[new_df['count'] > 200]

# sort by highest rating and lowest count
new_df = new_df.sort_values(by=['rating'], ascending=[False])

# top 100 movies
top_movies = new_df.head(3)

# sort top_movies by count low to high
top_movies = top_movies.sort_values(by=['count'], ascending=[True])

# iterate though each row in top_movies and try to get all the info
for index, row in top_movies.iterrows():
    lis = ['title', 'cover_url', 'full_size_cover_url', 'year', 'rating', 'votes', 'kind', 'runtime', 'color info', 'language', 'country', 'aspect ratio', 'sound mix', 'budget', 'opening weekend usa', 'gross usa', 'cumulative worldwide gross', 'genres', 'plot outline', 'plot', 'taglines', 'keywords', 'certificate', 'original air date', 'cast', 'cast characters', 'cast notes', 'cast votes', 'director', 'director notes', 'producer', 'producer notes', 'composer', 'cinematographer', 'editor', 'editor notes', 'writer', 'writer notes', 'production designer', 'art director', 'set decorator', 'costume designer', 'make up department', 'production manager', 'assistant director', 'sound department', 'special effects', 'visual effects', 'stunts', 'camera department', 'casting department', 'costume departmen', 'location management', 'music department', 'script department', 'transportation department', 'miscellaneous', 'thanks', 'akas', 'writer', 'writer notes', 'production manager', 'assistant director', 'sound department', 'special effects', 'visual effects', 'stunts', 'camera department', 'casting department', 'costume departmen', 'location management', 'music department', 'script department', 'transportation department', 'miscellaneous', 'thanks', 'akas', 'writer', 'writer notes', 'production manager', 'assistant director', 'sound department', 'special effects', 'visual effects', 'stunts', 'camera department', 'casting department', 'costume departmen', 'location management', 'music department', 'script department', 'transportation department', 'miscellaneous', 'thanks', 'akas', 'writer', 'writer notes', 'production manager', 'assistant director', 'sound department', 'special effects', 'visual effects', 'stunts', 'camera department', 'casting department', 'costume departmen', 'location management', 'music department', 'script department', 'transportation department', 'miscellaneous', 'thanks', 'akas', 'writer', 'writer notes', 'production manager', 'assistant director', 'sound department', 'special effects', 'visual effects', 'stunts', 'camera department', 'casting department', 'costume departmen', 'location management', 'music department', 'script department', 'transportation department', 'miscellaneous', 'thanks', 'akas', 'writer', 'writer notes', 'production manager', 'assistant director', 'sound department', 'special']
    # 
    for i in lis:
        try:
            movie = ia.get_movie(row['imdbId'])
            # check if the movie has the attribute
            if hasattr(movie, i):
                # if it does, add it to the top_movies dataframe
                top_movies.at[index, i] = getattr(movie, i)
            else:
                # if it doesn't, add None to the top_movies dataframe
                top_movies.at[index, i] = None

        except:
            # top_movies.at[index, i] = None
            print("error in " + i + " for " + str(row['imdbId']) + " " + str(row['title']))

print(
top_movies.head(2))