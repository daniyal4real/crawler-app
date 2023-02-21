from sqlalchemy import  Column, Integer, String
from config import Base

class News(Base):
    __tablename__ ="news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)