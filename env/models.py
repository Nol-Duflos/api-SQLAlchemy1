from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'Users'
    id:Mapped[int] = mapped_column(primary_key=True) #On créer une clef primaire pour les utilisateurs
    username:Mapped[str] = mapped_column(nullablr = False) 
    email_adress:Mapped[str]

class Comment(Base):
    __tablename__ = 'Comment'
    id:Mapped[int] = mapped_column(primary_key=True) #On créer une clef primaire pour les commentaire
    user_id:Mapped[int] = mapped_column(ForeignKey('user.id')) #On importe une clef étrangère (celle des utilisateurs)
    text:Mapped[str] = mapped_column(Text, nullable=False)
