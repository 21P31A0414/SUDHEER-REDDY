import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample movie data (replace with your own dataset)
movies = {
    'MovieID': [1, 2, 3, 4, 5],
    'Title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Inception'],
    'Genre': ['Drama', 'Crime', 'Action', 'Crime, Thriller', 'Sci-Fi, Action']
}
movies_df = pd.DataFrame(movies)

# Content-Based Filtering
def content_based_recommendations(movie_title, df=movies_df):
    """Recommends movies based on genre similarity."""

    # 1. Create TF-IDF vectors for movie genres
    tfidf = TfidfVectorizer(stop_words='english')  # Remove common words like 'the', 'a'
    tfidf_matrix = tfidf.fit_transform(df['Genre'])

    # 2. Calculate cosine similarity between movies
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # 3. Get the index of the movie that matches the title
    indices = pd.Series(df.index, index=df['Title']).drop_duplicates()
    idx = indices[movie_title]

    # 4. Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 5. Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 6. Get the scores of the 10 most similar movies (excluding the movie itself)
    sim_scores = sim_scores[1:11]

    # 7. Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # 8. Return the top 10 most similar movies
    return df['Title'].iloc[movie_indices]

# Collaborative Filtering (Simplified User-Based Example)
user_ratings = {
    'User1': {'The Shawshank Redemption': 5, 'The Godfather': 4, 'Pulp Fiction': 5},
    'User2': {'The Godfather': 5, 'The Dark Knight': 4, 'Inception': 5},
    'User3': {'The Shawshank Redemption': 4, 'Pulp Fiction': 3, 'The Dark Knight': 5}
}

def collaborative_recommendations(user, user_ratings=user_ratings):
  """Simple Collaborative Filtering (User based)"""

  if user not in user_ratings:
        return "User not found."

  user_rated_movies = user_ratings[user]
  similar_users = {}

  for other_user, other_user_ratings in user_ratings.items():
        if other_user != user:
            common_movies = set(user_rated_movies.keys()) & set(other_user_ratings.keys())
            if common_movies: # Only if they have rated movies in common
              similarity = sum(user_rated_movies[movie] * other_user_ratings[movie] for movie in common_movies)
              similar_users[other_user] = similarity
  if not similar_users:
      return "No similar users found."

  most_similar_user = max(similar_users, key=similar_users.get)
  recommendations = []

  for movie, rating in user_ratings[most_similar_user].items():
        if movie not in user_rated_movies:
            recommendations.append(movie)

  if not recommendations:
      return "No recommendations available."

  return recommendations


# Example usage
print("Content-Based Recommendations for 'The Godfather':")
print(content_based_recommendations('The Godfather'))

print("\nCollaborative Recommendations for 'User1':")
print(collaborative_recommendations('User1'))

print("\nCollaborative Recommendations for 'User4':")
print(collaborative_recommendations('User4'))
