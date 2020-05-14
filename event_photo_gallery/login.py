import string
import random
from flask_login import LoginManager

login = LoginManager()

def generate_passcode(size=12, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
