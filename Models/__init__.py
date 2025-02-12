from .User import User
from .Model import Model
from .Key import Key
from .Session import Session
from .Request import Request

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass