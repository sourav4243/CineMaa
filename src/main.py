import numpy as np
import pandas as pd
import ast
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Load the dataset
movies = pd.read_csv('./data/Top_10000_Movies_IMDb.csv')

# Select relevant columns
movies = movies[['Movie Name', 'Genre', 'Plot', 'Directors', 'Stars', 'Rating']]

# Function to convert string representation of list to actual list
def convertStringToList(obj):
    try:
        return ast.literal_eval(obj)
    except (ValueError, SyntaxError):
        return []

movies['Stars'] = movies['Stars'].apply(convertStringToList)
movies['Directors'] = movies['Directors'].apply(convertStringToList)

def returnFirstName(obj):
    if isinstance(obj, list) and obj:
        return [obj[0]]
    return []

movies['Directors'] = movies['Directors'].apply(returnFirstName)

# Splitting Plot into words
movies['Plot'] = movies['Plot'].apply(lambda x: x.split() if isinstance(x, str) else [])

# Remove spaces in between names in 'Directors', 'Stars', and 'Genre'
movies['Directors'] = movies['Directors'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['Stars'] = movies['Stars'].apply(lambda x: [i.replace(" ", "") for i in x])

# Function to convert comma-separated string to list for the genre column
def convertList(obj):
    if isinstance(obj, str):
        return [i.strip() for i in obj.split(',')]
    return []

movies['Genre'] = movies['Genre'].apply(convertList)
movies['Genre'] = movies['Genre'].apply(lambda x: [i.replace(" ", "") for i in x])

# Create 'tags' column for similarity calculation
movies['tags'] = movies['Genre'] + movies['Plot'] + movies['Directors'] + movies['Stars']

# Create a new DataFrame with 'Movie Name' and 'tags'
newData = movies[['Movie Name', 'tags']].copy()

newData.loc[:, 'tags'] = newData['tags'].apply(lambda x: " ".join(x).lower())

ps = PorterStemmer()
def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

newData.loc[:, 'tags'] = newData['tags'].apply(stem)
cv = CountVectorizer(max_features=5000, stop_words='english')

# Convert 'tags' to vectors
vectors = cv.fit_transform(newData['tags']).toarray()

# Check if the similarity matrix is already cached
similarity_cache_file = 'similarity_matrix.npy'

if os.path.exists(similarity_cache_file):
    similarity = np.load(similarity_cache_file)
else:
    similarity = cosine_similarity(vectors)
    np.save(similarity_cache_file, similarity)

# Main function to recommend movies
def recommend(movieName):
    if movieName not in newData['Movie Name'].values:
        print(f"Movie '{movieName}' not found in database.")
        return
    movieIndex = newData[newData['Movie Name'] == movieName].index[0]
    distances = similarity[movieIndex]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movies_list:
        print(newData.iloc[i[0]]['Movie Name'])
    print()

while True:
    movie = input("Enter the movie name: ")
    try:
        recommend(movie)
    except:
        print("Movie not found in the dataset")
    print()
    print("Do you want to continue? (y/n)")
    choice = input()
    if choice.lower() != 'y':
        break
