from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, select

db = SQLAlchemy()

class Session(db.Model):
  __tablename__ = "sessions"
  id: Mapped[int] = mapped_column(primary_key=True)
  user_id: Mapped[int]
  model_id: Mapped[int]
  created_at: Mapped[str]
  updated_at: Mapped[str]
  deleted_at: Mapped[str]
