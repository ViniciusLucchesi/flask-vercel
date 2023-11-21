from api.database import mongo
from api.models import User, UserResponse




def new_user(user: User) -> bool:
    """
    # new_user 
    
    Function responsible for inserting a new user in the database, 
    returning True if the user was inserted and False if some error occurred.

    ## ARGS:
    - user: User

    ## RETURN:
    - True -> if user was inserted\n
    - False -> if some error occurred
    """
    try:
        mongo.db.users.insert_one(user.__dict__)
        return True
    except Exception as e:
        print(e)
        return False


def get_all_users() -> list[UserResponse]:
    """
    # get_all_users

    Function responsible for returning all users in the database.

    ## RETURN:
    - list -> with all users in the database
    """
    users = list(mongo.db.users.find())
    return [UserResponse(**user).to_dict() for user in users]