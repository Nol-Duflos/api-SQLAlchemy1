from sqlalchemy import create_engine, text

#engine = create_engine("postgresql://fake_user:fake_password@localhost:54321/fake_database", echo = True) #Route vers notre base de données
engine = create_engine("sqlite://sample.db", echo = True)

with engine.connect() as connection:
    result = connection.execute(text('select "Salut !!"'))
    
    print(result.all())
