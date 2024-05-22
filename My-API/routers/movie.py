from fastapi import APIRouter
from fastapi import   Path, Query,  Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from service.movie import MovieService
from schemas.movies import Movie


movie_router = APIRouter()




@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])  # Método que devuelve películas
def get_movies() -> List[Movie]:
    db = Session()
    result=MovieService(db).get_movies()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

# Filtrado de películas por ID
@movie_router.get('/movies/{id}', tags=['movies'], status_code=200)  # Método de filtrado de películas
def get_movies_filtered(id: int = Path(ge=1, le=2000)):
    db = Session()
    result=MovieService(db).get_movies(id)
    if not result:
        return JSONResponse(status_code=404, content={'message':"No encontrado"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
    """
    for item in movies:
       if item["id"] == id:
         return JSONResponse(content=item)
    """
   

# Filtrado de películas por categoría
@movie_router.get('/movies/', tags=["movies"], status_code=200)
def get_movies_category(category: str = Query(min_length=5, max_length=15)):
    db = Session()
    result=MovieService(db).get_movies(category)
    if not result:
         return JSONResponse(status_code=404, content={'message':"No encontrado"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
    """
    movies_by_category = [item for item in movies if item["category"] == category]
    if not movies_by_category:
        return JSONResponse(content=[], status_code=404)
    return JSONResponse(content=movies_by_category, status_code=200)
      """

#agregamos pelicula
@movie_router.post('/movies', tags=['movies'], response_model=dict,status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content=movie.dict(), status_code=201)

#actualizacion de pelicula
@movie_router.put('/movies/{id}', tags=['movies'], status_code=200)
def update_movie(id: int, movie: Movie):
    db = Session()
    result=MovieService(db).get_movies(id)
    if not result:
         return JSONResponse(status_code=404, content={'message':"Pelicula no encontrada bro"})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message":"Se modifico la pelicula capo"})
    
    """
    for item in movies:
        if item["id"] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return JSONResponse(content=item, status_code=200)
    raise HTTPException(status_code=404, detail="Película no encontrada")
    """

#eliminacion de peliucla
@movie_router.delete('/movies/{id}', tags=['movies'], status_code=200)
def delete_movie(id: int):
    db = Session()
    result=db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message':"Pelicula no encontrada bro"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={'message':"Se elimino la pelicula maquina"})
    
    """
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(content=item, status_code=200)
    raise HTTPException(status_code=404, detail="Película no encontrada")
     """