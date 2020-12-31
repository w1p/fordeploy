from werkzeug.security import safe_str_cmp
from models.user import UserModel

# users = [User(1, "John", "4321")]
# uname_mapping = {u.username: u for u in users}
# uid_mapping = {u.id: u for u in users}


def authenticate(uname, pwd):
    # user = uname_mapping.get(uname, None)
    user = UserModel.findByUsername(uname)
    if user and safe_str_cmp(user.password, pwd):
        return user


def identity(pl):
    user_id = pl["identity"]
    return UserModel.findById(user_id)