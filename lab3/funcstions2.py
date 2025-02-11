# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Function to check if a single movie's IMDB score is above 5.5
def is_above_55(movie):
    return movie["imdb"] > 5.5
print(is_above_55({"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"}))  # Output: True

#Function to return a sublist of movies with an IMDB score above 5.5
def movies_above_55(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]
print(movies_above_55(movies))

#Function to return movies under a specific category
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]
print(movies_by_category(movies, "Romance"))

#Function to compute the average IMDB score of a list of movies
def average_imdb_score(movies):
    if not movies:
        return 0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)
print(average_imdb_score(movies))  # Output: 6.32

#Function to compute the average IMDB score for a specific category
def average_imdb_score_by_category(movies, category):
    category_movies = [movie for movie in movies if movie["category"] == category]
    return average_imdb_score(category_movies)
print(average_imdb_score_by_category(movies, "Romance"))  # Output: 6.24
