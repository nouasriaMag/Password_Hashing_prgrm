import bcrypt
from typing import Tuple
from datetime import datetime

def hash_pwd(password:str, rounds=12) -> bytes:
    pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
    print(pwd)
    return pwd

def check_pwd(password:str, hash:bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hash)

class UserAuth:
    def __init__(self):
        self.users = {}
        self.login_attempts = {}
        self.max_attemps = 3
        self.lockout_minutes = 15

    def add_user(self, username:str, password:str) -> bool:
        if username in self.users:
            return False

        self.users[username] = {
            'pwd_hash': hash_pwd(password),
            'created_at': datetime.now(),
            'pwd_rounds': 12
        }
        return True

    def login(self):
        pass

    def _is_locked(self,username:str) -> bool:
        if username not in self.login_attempts:
            return False

        attempts, last_attempt = self.login_attempts[username]
        if attempts >= self.max_attempts:
            mins_passed = (datetime.now() - last_attempt).total_seconds() / 60
            if mins_passed < self.lockout_minutes:
                return True
            del self.login_attempts[username]
        return False

    def _track_attempts(self, username:str):
        now = datetime.now()
        if username in self.login_attempts:
            attempts, _ = self.login_attempts[username]
            self.login_attempts[username] = (attempts +1, now)
