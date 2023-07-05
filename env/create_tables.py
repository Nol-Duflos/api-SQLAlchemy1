#Ici, on vas importer les models et engine
#Et créer un code qui en l'executant, vas créer des tables à partir des models.

from models import Base, User, Comment
from connect import engine

print("CREATING TABLES >>>")
Base.metadata.create_all(bind=engine)