from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from contextlib import contextmanager


SQLALCHEMY_DATABASE_URL = "mysql://root:my-secret-pw@db/sentiment_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=3600)

CustomizedDBSessionFactory =  sessionmaker(autocommit=False, autoflush=False, bind=engine)



# Define a context manager for the session
@contextmanager
def CustomizedDBSession():
    session = CustomizedDBSessionFactory()
    try:
        yield session
        session.commit()
    except PendingRollbackError as rollback_error:
        # Roll back the transaction and handle the error
        session.rollback()
        print(f"PendingRollbackError: {rollback_error}")
        # Additional error handling if needed
    except Exception as e:
        # Roll back the transaction and handle other exceptions
        session.rollback()
        print(f"Error: {e}")
        # Additional error handling if needed
    finally:
        session.close()


Base = declarative_base()