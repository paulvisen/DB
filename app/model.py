

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String,TEXT,VARCHAR,DATETIME
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class Report(BaseModel):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    authorid = Column(Integer)
    body = Column(TEXT)
    type = Column(VARCHAR)
    typeid = Column(Integer)
    timestamp = Column(DATETIME)



class AvatarVoice(BaseModel):
    __tablename__='avatarvoices'



