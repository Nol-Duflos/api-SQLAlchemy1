import models import Base, User, Comment
import connect import engine

print("CREATING TABLE >>>> ")
Base.metadata.create_all(bind=engine)