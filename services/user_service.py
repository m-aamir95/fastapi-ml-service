from sqlalchemy.orm import Session

from database.db_schema_models import User

from abc import ABC, abstractmethod


class UserService(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def create_user(self, username : str, hashed_password : str):
        pass


class SqlAlchemyUserService(UserService):

    def __init__(self, db_session : Session):
        self.db_session = db_session

    def create_user(self, username : str, hashed_password : str):

        new_user = User(username=username, hashed_password=hashed_password)
    
        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user) # Used to synchronize sqlalchemy with the databse

        return new_user
    