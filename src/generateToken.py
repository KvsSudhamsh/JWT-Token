import jwt
import datetime

class GenerateToken:
    def __init__(self):
        self.secret_key = "MY_SECRET_KEY"

    def generate_token(self, user_id) -> str:
        payload = {
            "user_id" : user_id,
            "exp" : datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds = 60)
        }
        token = jwt.encode(payload, self.secret_key, algorithm = "HS256")
        return token
