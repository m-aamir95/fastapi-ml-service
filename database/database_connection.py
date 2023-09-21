from sqlalchemy import create_engine
from sqlalchemy.exc.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql://root:my-secret-pw@localhost/your_database_name"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal =  sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()