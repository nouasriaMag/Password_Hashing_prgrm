import bcrypt
from typing import Tuple
from datetime import datetime

def hash_pwd(password:str, rounds=12) -> bytes:
    pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
    print(pwd)
    return pwd

<<<<<<< HEAD
def check_pwd(password:str, hash:bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hash)
=======
from pyargon2 import hash

#for loop for a hash + input of a password
>>>>>>> refs/remotes/origin/main
