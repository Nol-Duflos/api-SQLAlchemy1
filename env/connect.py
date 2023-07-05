from sqlalchemy import create_engine, text

engine = create_engine("postgresql://utilisateur:motdepasse@localhost:port/nom_base_de_donnees", echo = True) #Route vers notre base de données

with engine.connect() as connection:
    result = connection.execute(text('select "Salut !!"'))
    
    print(result.all())
