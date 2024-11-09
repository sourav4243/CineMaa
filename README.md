# Movie Recommendation System in Python

## Overview

This project is a Movie Recommendation System built using Python. It leverages content-based filtering to suggest movies to users based on the similarity of movie attributes such as genres, plot, directors, and stars.

## Features

- **Content-based Filtering**: Recommends movies based on the content similarity (genres, plot, directors, stars).
- **Stemming**: Uses PorterStemmer to reduce words to their root form for better similarity matching.
- **Cosine Similarity**: Calculates the similarity between movies using cosine similarity on vectorized movie tags.
- **Caching**: Caches the similarity matrix to improve performance on subsequent runs.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Sourav4243/CineMaa.git
    cd CineMaa
    ```

2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Prepare the dataset:
    - Ensure you have the dataset `Top_10000_Movies_IMDb.csv` in the `data` directory.

2. Run the recommendation script:
    - Use the script to generate movie recommendations.

    ```sh
    python src/main.py
    ```

## Project Structure

- `data/`: Contains the dataset file.
  - `Top_10000_Movies_IMDb.csv`: The dataset file containing movie information.
- `src/`: Contains the source code.
  - `main.py`: The main script for preprocessing the data and generating recommendations.
- `README.md`: Provides an overview of the project, installation instructions, usage, etc.
- `requirements.txt`: Lists the dependencies required to run the project.
- `LICENSE`: Specifies the license under which the project is distributed.

## How It Works

1. **Data Loading**:
    - The dataset is loaded using pandas.

2. **Data Preprocessing**:
    - Relevant columns are selected.
    - String representations of lists are converted to actual lists.
    - Spaces are removed from names in the `Directors`, `Stars`, and `Genre` columns.
    - A `tags` column is created by combining `Genre`, `Plot`, `Directors`, and `Stars`.
    - The tags are joined into a single string and converted to lowercase.
    - Words in the tags are stemmed using PorterStemmer.

3. **Vectorization**:
    - The tags are converted to vectors using `CountVectorizer`.

4. **Similarity Calculation**:
    - Cosine similarity is calculated between the vectors.
    - The similarity matrix is cached to improve performance on subsequent runs.

5. **Recommendation**:
    - The `recommend` function takes a movie name as input and prints the top 5 similar movies based on cosine similarity.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- [Scikit-learn](https://scikit-learn.org/) for the machine learning algorithms.
- [Pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/) for data manipulation and analysis.
- [NLTK](https://www.nltk.org/) for natural language processing tools.
