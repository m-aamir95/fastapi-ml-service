from sqlalchemy.orm import Session
from sqlalchemy.exc import PendingRollbackError

from database.db_schema_models import User

from abc import ABC, abstractmethod

from fastapi import HTTPException

from typing import Optional

class UserService(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def create_user(self, username : str, hashed_password : str):
        pass

    @abstractmethod
    def verify_user_login(self, username: str, hashed_password : str) -> Optional[User]:
        pass    

class SqlAlchemyUserService(UserService):

    def __init__(self, db_session : Session):
        self.db_session = db_session

    def create_user(self, username : str, hashed_password : str):

        new_user = User(username=username, hashed_password=hashed_password)

        try:
            # Check if the username already exists
            matching_users = self.db_session.query(User).filter(User.username == new_user.username)

        except PendingRollbackError as rollback_error:
            self.db_session.rollback()
            print(f"PendingRollbackError: {rollback_error}")
        except Exception as e:
            self.db_session.rollback()
            print(f"Error: {e}")
        finally:
            # The session is automatically closed when the block exits
            self.db_session.close()
    
        if matching_users:
            for user in matching_users:
                raise HTTPException(status_code=422, detail="Username already exists")


        try:
            # Username does not already exist, go ahead and create a new user
            self.db_session.add(new_user)
            self.db_session.commit()
            self.db_session.refresh(new_user) # Used to synchronize sqlalchemy with the databse

        except PendingRollbackError as rollback_error:
            self.db_session.rollback()
            print(f"PendingRollbackError: {rollback_error}")
        except Exception as e:
            self.db_session.rollback()
            print(f"Error: {e}")
        finally:
            # The session is automatically closed when the block exits
            self.db_session.close()

        return new_user


    def verify_user_login(self, username: str, hashed_password : str) -> Optional[User  ]:
        
        user_to_verify = User(username=username, hashed_password=hashed_password)

        matched_user = None
        try:
            #Check if the username and password exists
            matched_user = self.db_session.query(User).filter(User.username == user_to_verify.username, 
                                                    User.hashed_password == user_to_verify.hashed_password).first()

        except PendingRollbackError as rollback_error:
            self.db_session.rollback()
            print(f"PendingRollbackError: {rollback_error}")
        except Exception as e:
            self.db_session.rollback()
            print(f"Error: {e}")
        finally:
            # The session is automatically closed when the block exits
            self.db_session.close()

        if matched_user:
            return matched_user
        else:
            return None