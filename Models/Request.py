from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, select

db = SQLAlchemy()

class Request(db.Model):
  __tablename__ = "requests"
  id: Mapped[int] = mapped_column(primary_key=True)
  session_id: Mapped[int]
  type: Mapped[str]
  request: Mapped[str]
  response: Mapped[str]
  created_at: Mapped[str]
  updated_at: Mapped[str]
  deleted_at: Mapped[str]