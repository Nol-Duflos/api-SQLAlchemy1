from models import User, Comment
from sqlalchemy.orm import Session
from connect import engine

session = Session(bind=engine)

#On vas créer des objets qui représentent la Data
Jonas = User(
    username = 'Jonas',
    email_adress = 'jonas.varga@gmail.com',
    comment = [
        Comment(text = "Trés bon tutoriel, hate de voir la suite :D"),
        Comment(text = "Attention, il ya une erreur à 2.14min de la video [...]"), 
        Comment(text = "Je suis trs fan de ce groupe, hâte qu'ils viennent dans ma ville !!")
    ]
)

Pauline = User(
    username = 'Powpow',
    email_adress = 'pauline@gmail.com',
    comment = [
        Comment(text = "What's up ?"),
        Comment(text = "Naaan c'est pas comme ça que ça marche"), 
        Comment(text = "Cette leçon sur youtube m'a debloqué de mon exercice de Math")
    ]
)

Amelie = User(
    username = 'AmeYuki',
    email_adress = 'ameyukilili@protonmail.com'
)

session.add_all([Jonas, Pauline, Amelie])

session.commit()