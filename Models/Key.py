from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, select

db = SQLAlchemy()

class Key(db.Model):
  __tablename__ = "keys"
  id: Mapped[int] = mapped_column(primary_key=True)
  user_id: Mapped[int]
  client_id: Mapped[str]
  secret_key: Mapped[str]
  created_at: Mapped[str]
  updated_at: Mapped[str]
  deleted_at: Mapped[str]
