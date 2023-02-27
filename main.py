import pandas as pd

# Read the data
df = pd.read_csv(r"C:\Users\saket\Desktop\ratings.csv").sort_values(by=['movieId']) 
imdb_id = pd.read_csv(r"C:\Users\saket\Desktop\links.csv").sort_values(by=['movieId'])

# average rating of each movie
df['rating'] = df.groupby('movieId')['rating'].transform('mean')

# only 3 digits after decimal in rating
df['rating'] = df['rating'].apply(lambda x: round(x, 3))

# count number of times each movie is rated
df['count'] = df.groupby('movieId')['movieId'].transform('count')

# dataframe of movieId and average rating and count
new_df = df[['movieId', 'rating', 'count']].drop_duplicates()

# add tmdbId and imdbId to new_df
new_df = pd.merge(new_df, imdb_id)

import imdb

# Create an IMDb access object
ia = imdb.IMDb()

import pandas as pd
new_df = pd.read_csv("new_df.csv")

new_df = pd.read_csv("new_df.csv")
# all the that has more than 200 count
new_df = new_df[new_df['count'] > 100]

# sort by highest rating and lowest count
new_df = new_df.sort_values(by=['rating'], ascending=[False])

# rating > 4
new_df = new_df[new_df['rating'] > 3.9]

# top 100 movies
top_movies = new_df.head(1000)

# sort top_movies by count low to high 
# top_movies = top_movies.sort_values(by=['count'], ascending=[True])

# reset the index
top_movies = top_movies.reset_index(drop=True)
print(len(top_movies))
# top_movies.head(20)




# sort top_movies by 

# check if csv file exists
import os.path
columns=['movieId', 'rating', 'count', 'imdbId', 'tmdbId', 'title','cover url', 'full-size cover url']
if not os.path.exists('top_movies.csv'):
    # create a csv file
    top_movies_file = pd.DataFrame(columns=columns)
    # save the csv file
    top_movies_file.to_csv('top_movies.csv', index=True)
    # set the default last_index to 0
    last_index = 0

else:
    # continue from the last row of top_movies.csv
    top_movies_file = pd.read_csv('top_movies.csv')

    # get the last row of top_movies_file
    last_row = top_movies_file.tail(1)

    try:
        print(last_row['movieId'][0])
    except:
        print(last_row['movieId'])

    # save the last movieId
    last_movieId = last_row['movieId'].iloc[0]

    # get the index of top_movies where movieId is equal to last_movieId
    last_index = top_movies[top_movies['movieId'] == last_movieId].idxmax()['movieId']+1
    print(last_index)


# iterate though last_index
for index, row in top_movies[last_index:].iterrows():
#     # get movie object
    try:
        movie = ia.get_movie(row['imdbId'])
    except:
        pass
    
    # new column list
    new_columns = ['title', 'cover url', 'full-size cover url']

    # iterate through new_columns
    for column in new_columns:
        try:
            # add the column to row
            row.at[column] = movie[column]
        except:
            # if column is not found then add nan
            row.at[column] = float('nan')
    # add the row to a csv file
    row = pd.DataFrame([row])
    row.to_csv('top_movies.csv', mode='a', header=False, index=True, columns=columns)




# import imdb

# # Create an IMDb access object
# ia = imdb.IMDb()

# import pandas as pd
# new_df = pd.read_csv("new_df.csv")

# # all the that has more than 200 count
# new_df = new_df[new_df['count'] > 200]

# # sort by highest rating and lowest count
# new_df = new_df.sort_values(by=['rating'], ascending=[False])

# # top 100 movies
# top_movies = new_df.head(3)

# # sort top_movies by count low to high
# top_movies = top_movies.sort_values(by=['count'], ascending=[True])



# # iterate though each row in top_movies and try to get all the info
# for index, row in top_movies.iterrows():
#     lis = ['title', 'cover_url', 'full_size_cover_url', 'year', 'rating', 'votes', 'kind', 'runtime', 'color info', 'language', 'country', 'aspect ratio', 'sound mix', 'budget', 'opening weekend usa', 'gross usa', 'cumulative worldwide gross', 'genres', 'plot outline', 'plot', 'taglines', 'keywords', 'certificate', 'original air date', 'cast', 'cast characters', 'cast notes', 'cast votes', 'director', 'director notes', 'producer', 'producer notes', 'composer', 'cinematographer', 'editor', 'editor notes', 'writer', 'writer notes', 'production designer', 'art director', 'set decorator', 'costume designer', 'make up department', 'production manager', 'assistant director', 'sound department', 'special effects', 'visual effects', 'stunts', 'camera department', 'casting department', 'costume departmen', 'location management', 'music department', 'script department', 'transportation department', 'miscellaneous', 'thanks', 'akas', 'writer', 'writer notes', 'production manager', 'assistant director', 'sound department', 'special effects', 'visual effects', 'stunts', 'camera department', 'casting department', 'costume departmen', 'location management', 'music department', 'script department', 'transportation department', 'miscellaneous', 'thanks', 'akas', 'writer', 'writer notes', 'production manager', 'assistant director', 'sound department', 'special effects', 'visual effects', 'stunts', 'camera department', 'casting department', 'costume departmen', 'location management', 'music department', 'script department', 'transportation department', 'miscellaneous', 'thanks', 'akas', 'writer', 'writer notes', 'production manager', 'assistant director', 'sound department', 'special effects', 'visual effects', 'stunts', 'camera department', 'casting department', 'costume departmen', 'location management', 'music department', 'script department', 'transportation department', 'miscellaneous', 'thanks', 'akas', 'writer', 'writer notes', 'production manager', 'assistant director', 'sound department', 'special effects', 'visual effects', 'stunts', 'camera department', 'casting department', 'costume departmen', 'location management', 'music department', 'script department', 'transportation department', 'miscellaneous', 'thanks', 'akas', 'writer', 'writer notes', 'production manager', 'assistant director', 'sound department', 'special']
#     # 
#     for i in lis:
#         try:
#             movie = ia.get_movie(row['imdbId'])
#             # check if the movie has the attribute
#             if hasattr(movie, i):
#                 # if it does, add it to the top_movies dataframe
#                 top_movies.at[index, i] = getattr(movie, i)
#             else:
#                 # if it doesn't, add None to the top_movies dataframe
#                 top_movies.at[index, i] = None

#         except:
#             # top_movies.at[index, i] = None
#             print("error in " + i + " for " + str(row['imdbId']) + " " + str(row['title']))

# print(
# top_movies.head(2))