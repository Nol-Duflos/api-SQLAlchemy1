from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from typing import List


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'Users'
    id:Mapped[int] = mapped_column(primary_key=True) #On créer une clef primaire pour les utilisateurs
    username:Mapped[str] = mapped_column(nullable=False) 
    email_adress:Mapped[str]
    comment:Mapped[List["Comment"]] =relationship(back_populate = 'user')

    def __repr__(self) -> str:
        return f"<User username={self.username}>"

class Comment(Base):
    __tablename__ = 'comments'
    id:Mapped[int] = mapped_column(primary_key=True) #On créer une clef primaire pour les commentaire
    user_id:Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False) #On importe une clef étrangère (celle des utilisateurs)
    text:Mapped[str] = mapped_column(Text, nullable=False) #On ne permet pas aux utilisateurs d'utiliser des 
    user:Mapped["User"] =relationship(back_populate='comments')

    def __repr__(self):
        return f"<Comment text={self.text} by {self.user.username}>"