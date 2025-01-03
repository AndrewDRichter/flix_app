from movies.repository import MovieRepository


class MovieService:

    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self):
        return self.movie_repository.get_movies()

    def create_movies(self, title, release_date, genre, actors, summary):
        movie = dict(
            title=title,
            release_date=release_date,
            genre=genre,
            actors=actors,
            summary=summary,
        )
        return self.movie_repository.create_movie(movie)

    def get_movie_stats(self):
        return self.movie_repository.get_movie_stats()
