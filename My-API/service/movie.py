from models.movie import Movie as MovieModel
from schemas.movies import Movie

class MovieService():
   #cada vez que llamamos a este servicio se envia a la base de datos
    def __init__(self,db) -> None:
        self.db = db
    def get_movies(self):
        result=self.db.query(MovieModel).all()
        return result
    def get_movies(self, id):
        result=self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    def get_movies(self, category):
        result=self.db.query(MovieModel).filter(MovieModel.category == category).first()
        return result  
    def create_movie(self, movie: Movie):
        new_movie=MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return
    
    def update_movie(self, id: int, data:Movie):
        movie = self.get_movies(id)
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return
    
        