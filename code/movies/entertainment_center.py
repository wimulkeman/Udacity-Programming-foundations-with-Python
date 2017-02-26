import media
import fresh_tomatoes

toy_store = media.Movie(
    'Toy Story',
    'A story of a boy and his toys that come to life',
    'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
    'https://www.youtube.com/watch?v=KYz2wyBy3kc'
)

avatar = media.Movie(
    'Avatar',
    'A marine on an alien planet',
    'https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg',
    'https://www.youtube.com/watch?v=5PSNL1qE6VY'
)

sherlock_holmes = media.Movie(
    'Sherlock Holmes',
    'Nothing escapes them',
    'https://upload.wikimedia.org/wikipedia/en/e/e0/Sherlock_holmes_ver5.jpg',
    'https://www.youtube.com/watch?v=J7nJksXDBWc'
)

movies = [toy_store, avatar, sherlock_holmes]
# fresh_tomatoes.open_movies_page(movies)
# print media.Movie.VALID_RATINGS
# print media.Movie.__doc__

# Output: Movie
print media.Movie.__name__

# Output: media
print media.Movie.__module__
