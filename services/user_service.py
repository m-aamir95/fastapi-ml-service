from sqlalchemy.orm import Session

from database.db_schema_models import User

from abc import ABC, abstractmethod

from fastapi import HTTPException


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

        # Check if the username already exists
        matching_users = self.db_session.query(User).filter(User.username == new_user.username)
        
       
        if matching_users:
            for user in matching_users:
                raise HTTPException(status_code=422, detail="Username already exists")


        # Username does not already exist, go ahead and create a new user
        self.db_session.add(new_user)
        self.db_session.commit()
        self.db_session.refresh(new_user) # Used to synchronize sqlalchemy with the databse

        return new_user


    def verify_user_login(self, username: str, hashed_password : str):
        
        user_to_verify = User(username=username, hashed_password=hashed_password)

        #Check if the username and password exists
        matched_user = self.db_session.query(User).filter(User.username == user_to_verify.username, 
                                                           User.hashed_password == user_to_verify.hashed_password).first()

        
        if matched_user:
            return matched_user
        else:
            None