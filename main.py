import numpy as np
import pandas as pd
import ast
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
movies = pd.read_csv('Top_10000_Movies_IMDb.csv')

# Select relevant columns
movies = movies[['Movie Name', 'Genre', 'Plot', 'Directors', 'Stars', 'Rating']]

# Function to convert string representation of list to actual list
def convertStringToList(obj):
    try:
        return ast.literal_eval(obj)
    except (ValueError, SyntaxError):
        return []

# Apply the conversion function to 'Stars' and 'Directors' columns
movies['Stars'] = movies['Stars'].apply(convertStringToList)
movies['Directors'] = movies['Directors'].apply(convertStringToList)

# Function to return the first name in a list
def returnFirstName(obj):
    if isinstance(obj, list) and obj:
        return [obj[0]]
    return []

# Apply the function to 'Directors' column
movies['Directors'] = movies['Directors'].apply(returnFirstName)

# Split 'Plot' into words
movies['Plot'] = movies['Plot'].apply(lambda x: x.split() if isinstance(x, str) else [])

# Remove spaces in between names in 'Directors', 'Stars', and 'Genre'
movies['Directors'] = movies['Directors'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['Stars'] = movies['Stars'].apply(lambda x: [i.replace(" ", "") for i in x])

# Function to convert comma-separated string to list
def convertList(obj):
    if isinstance(obj, str):
        return [i.strip() for i in obj.split(',')]
    return []

# Apply the conversion function to 'Genre' column
movies['Genre'] = movies['Genre'].apply(convertList)

# Remove spaces in between genre names
movies['Genre'] = movies['Genre'].apply(lambda x: [i.replace(" ", "") for i in x])

# Create 'tags' column by combining 'Genre', 'Plot', 'Directors', and 'Stars'
movies['tags'] = movies['Genre'] + movies['Plot'] + movies['Directors'] + movies['Stars']

# Create a new DataFrame with 'Movie Name' and 'tags'
newData = movies[['Movie Name', 'tags']]

# Join the list of tags into a single string and convert to lowercase
newData['tags'] = newData['tags'].apply(lambda x: " ".join(x).lower())

# Initialize PorterStemmer
ps = PorterStemmer()

# Function to stem words
def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

# Apply stemming to 'tags' column
newData['tags'] = newData['tags'].apply(stem)

# Initialize CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')

# Convert 'tags' to vectors
vectors = cv.fit_transform(newData['tags']).toarray()

# Calculate cosine similarity
similarity = cosine_similarity(vectors)

# Function to recommend movies
def recommend(movie):
    movie_index = newData[newData['Movie Name'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movies_list:
        print(newData.iloc[i[0]]['Movie Name'])

# Example usage
if __name__ == "__main__":
    print("Recommendations for 'The Godfather':")
    recommend('The Godfather')


