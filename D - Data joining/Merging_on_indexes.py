import pandas as pd


###### merging in one index  

# make id is the index
movies = pd.read_csv('tmdb_movies.csv' ,index_col =['id'])
print(movies.head())

# creat the merge on the index
movies_taglne = movies.merge(taglines, on ='id', how = 'left')
print(movies_taglne.head())


###### merging in multiple index  

# make another index from another file 
casts = pd.read_csv('tmdb_casts.csv' ,index_col =['cast_id'])
print(casts.head())

# creat the merge on multiple indexes
movies_taglne = movies.merge(casts, on =['id' , 'cast_id'], how = 'left')
print(movies_taglne.head())


# any merge type can do the index merge عادي
