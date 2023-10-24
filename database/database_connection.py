from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql://root:my-secret-pw@127.0.0.1/sentiment_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

CustomizedDBSessionFactory =  sessionmaker(autocommit=False, autoflush=False, bind=engine)
CustomizedDBSession = CustomizedDBSessionFactory()

Base = declarative_base()