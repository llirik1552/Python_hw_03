from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    user_id = Column(Integer, primary_key=True)
    level = Column(String)
    education_form = Column(String)
    subject_id = Column(Integer)

# Настройка базы данных
DATABASE_URL = "postgresql://postgres:123@localhost:5432/QA"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

