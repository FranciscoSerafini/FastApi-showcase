import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base #manipulacion de tablas


sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__)) #leemos el directorio de database
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}" #url de la base de datos
Engine = create_engine(database_url, echo=True)
Session = sessionmaker(bind=Engine)
Base = declarative_base()