#On a importé des données dans notre bdd
#Maintenant, on vas selectionner des items dans notre bdd
from persisting import session
from models import User, Comment

from sqlalchemy import select

statement = select(User).where(User.username.in_(['Jonas', 'Pauline']))

result = session.scalars(statement)

for user in result:
    print(user)