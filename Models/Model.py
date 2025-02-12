from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, select

db = SQLAlchemy()

class Model(db.Model):
  __tablename__ = "models"
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str]
  domain: Mapped[str]
  url: Mapped[str]
  client_id: Mapped[str]
  secret_key: Mapped[str]
  created_at: Mapped[str]
  updated_at: Mapped[str]
  deleted_at: Mapped[str]
