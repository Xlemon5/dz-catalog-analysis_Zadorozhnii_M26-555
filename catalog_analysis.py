import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021,
     "genres": {"sci-fi", "drama"}, "rating": 8.6,
     "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019,
     "genres": {"comedy", "drama"}, "rating": 7.1,
     "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016,
     "genres": {"thriller", "drama"}, "rating": 6.4,
     "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023,
     "genres": {"sci-fi", "action"}, "rating": 5.9,
     "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014,
     "genres": {"comedy"}, "rating": 7.8,
     "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020,
     "genres": {"thriller", "mystery"}, "rating": 8.9,
     "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022,
     "genres": {"drama"}, "rating": 4.8,
     "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024,
     "genres": {"sci-fi", "drama"}, "rating": 9.2,
     "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011,
     "genres": {"comedy"}, "rating": 6.0,
     "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018,
     "genres": {"action", "thriller"}, "rating": 7.3,
     "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# STAGE_1
def average_rating(movies):
    total = 0
    for movie in movies:
        total += movie['rating']
    return round(total/len(movies), 1)
        
def catalog_age_stats(movies, current_year=2026):
    newest = 9999
    oldest = -1
    average_age = 0
    age_film = 0
    for movie in movies:
        age_film = current_year - movie['year'] 
        newest = min(newest, age_film)
        oldest = max(oldest, age_film)
        average_age += age_film
    return (oldest, newest, math.ceil(average_age/len(movies))) 

def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"

#STAGE_2
def rating_tier(rating):
    if rating >= 9:
        category = "шедевр"
    elif rating >= 7:
        category = "хорошо"
    elif rating >= 5:
        category = "средне"
    else:
        category = "слабо"

    return category if rating >= 0 else "некорректная оценка"

def decade_label(year):
    match year:
        case year if year > 2020:
            return "новые"
        case year if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"
        
        
#STAGE_3  
print("Названия фильмов, которые не относятся к жанру комедии")
for movie in movies:
    if 'comedy' in movie['genres']:
        continue
    print(" -", movie['title'])

ind = 0
while ind < len(movies):
    if movies[ind]['rating'] > 9.0:
        print(f"Найден шедевр: {movies[ind]['title']}" 
              f"(рейтинг: {movies[ind]['rating']})")
        break
    ind += 1
else:
    print("Шедевров не найдено")
        
def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:      
        if movie['duration_min'] > threshold:
            count += 1
    return count


#STAGE 4
def normalize_title(title):
    words = title.split()
    normalized_words = [word[0].upper() + word[1:] for word in words]
    return " ".join(normalized_words)

def make_slug(title):
    return title.lower().replace(" ", "-")
    
def format_report_line(movie):
    sorted_genres = ", ".join(sorted(movie["genres"]))
    return (f'"{movie["title"]}" ({movie["year"]}) — {movie["rating"]}/10, '
            f'{duration_in_hours(movie["duration_min"])}, жанры: {sorted_genres}')


#STAGE5
def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]



#STAGE6

def count_by_genre(movies):
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts

def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography

highly_rated = {movie["title"]: movie["rating"] for movie in movies 
                if movie["rating"] > average_rating(movies)}


#STAGE7
def all_genres(movies):
    result = set()
    for movie in movies:
        result.update(movie["genres"])
    return result

def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])

def genres_only_in_one(movies_a, movies_b):
    genres_a = set()
    for movie in movies_a:
        genres_a.update(movie["genres"])

    genres_b = set()
    for movie in movies_b:
        genres_b.update(movie["genres"])

    return genres_a - genres_b


#STAGE8
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie 

#Демонстрация работы
for movie in iter_high_rated(movies):
    print(format_report_line(movie))
    
total_duration = sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)

    
#STAGE9
def build_report(movies):
    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет")
    print()

    print("Топ-3 фильма:")
    top_3_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)[:3]
    for movie in top_3_movies:
        print("  " + format_report_line(movie))
    print()

    print("Фильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    sorted_counts = sorted(genre_counts.items(), key=lambda item: item[1], reverse=True)
    for genre, count in sorted_counts:
        print(f"  {genre} — {count}")
    print()

    genres_list = sorted(all_genres(movies))
    print(f"Все жанры каталога: {', '.join(genres_list)}")


if __name__ == "__main__":
    build_report(movies)