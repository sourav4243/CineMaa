# Movie Recommendation system in python

## Overview

This project is a Movie Recommendation System built using Python. It leverages various machine learning algorithms to suggest movies to users based on their preferences and viewing history.

## Features

- **User-based Collaborative Filtering**: Recommends movies based on the similarity between users.
- **Item-based Collaborative Filtering**: Recommends movies based on the similarity between items (movies).
- **Content-based Filtering**: Recommends movies based on the content similarity (genres, actors, directors, etc.).
- **Hybrid Filtering**: Combines multiple recommendation strategies to improve accuracy.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/movierecommendation.git
    cd movierecommendation
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Prepare the dataset:
    - Ensure you have a dataset of movies and user ratings. You can use datasets like [MovieLens](https://grouplens.org/datasets/movielens/).

2. Preprocess the data:
    - Run the preprocessing script to clean and prepare the data for training.

    ```sh
    python preprocess.py
    ```

3. Train the model:
    - Train the recommendation model using the prepared data.

    ```sh
    python train.py
    ```

4. Generate recommendations:
    - Use the trained model to generate movie recommendations for a user.

    ```sh
    python recommend.py --user_id <USER_ID>
    ```

## Project Structure

- `data/`: Contains the dataset files.
- `preprocess.py`: Script for data preprocessing.
- `train.py`: Script for training the recommendation model.
- `recommend.py`: Script for generating recommendations.
- `models/`: Contains the trained models.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and model experimentation.
- `requirements.txt`: List of dependencies.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [MovieLens](https://grouplens.org/datasets/movielens/) for providing the dataset.
- [Scikit-learn](https://scikit-learn.org/) for the machine learning algorithms.
- [Pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/) for data manipulation and analysis.
