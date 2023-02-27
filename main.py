from app.keys import token
from app.disk import run

if __name__ == '__main__':
    my_token = token.get_token()
    run.app(my_token)
