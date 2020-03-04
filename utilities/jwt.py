import jwt

JWT_SECRET = 'helloworld'


def encode_jwt(payload):
    user_id = int(payload)
    return jwt.encode({'payload': user_id}, JWT_SECRET, algorithm='HS256')


def decode_jwt(jwt_string):
    return jwt.decode(jwt_string, JWT_SECRET, algorithm='HS256').get('payload')
