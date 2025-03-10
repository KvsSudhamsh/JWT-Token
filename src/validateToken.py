import jwt
import constant as const

class Validate:
    def validate_token(self, token):
        try:
            decoded = jwt.decode(token, const.SECRET_KEY, algorithms = "HS256")
            return decoded
        except jwt.ExpiredSignatureError:
            return "Token has expired"
        except jwt.InvalidTokenError:
            return "Invalid token"