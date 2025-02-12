from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, select

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = "users"
  id: Mapped[int] = mapped_column(primary_key=True)
  email: Mapped[str]
  password: Mapped[str]
  created_at: Mapped[str]
  updated_at: Mapped[str]
  deleted_at: Mapped[str]
