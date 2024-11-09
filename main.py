import numpy as np
import pandas as pd
import ast

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
movies['Genre'] = movies['Genre'].apply(lambda x: [i.replace(" ", "") for i in x])

# Function to convert comma-separated string to list
def convertList(obj):
    if isinstance(obj, str):
        return obj.split(',')
    return []

# Apply the conversion function to 'Genre' column
movies['Genre'] = movies['Genre'].apply(convertList)

# Create 'tags' column by combining 'Genre', 'Plot', 'Directors', and 'Stars'
movies['tags'] = movies['Genre'] + movies['Plot'] + movies['Directors'] + movies['Stars']

# Create a new DataFrame with 'Movie Name' and 'tags'
newData = movies[['Movie Name', 'tags']]

# Join the list of tags into a single string and convert to lowercase
newData['tags'] = newData['tags'].apply(lambda x: " ".join(x).lower())

# Display the first few rows of the new DataFrame
print(newData.head())


