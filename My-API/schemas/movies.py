from pydantic import BaseModel, Field
from typing import Optional, List

class Movie(BaseModel):  # Esta clase lo que hace es heredar de BaseModel
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2024)
    rating: float
    category: str

    # Clase extra para configuración inicial
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "My movie",
                "overview": "Descripción de la película",
                "year": 2022,
                "rating": 9.8,
                "category": "Acción"
            }
        }
