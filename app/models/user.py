import random
import string
import urllib
import hashlib
import hmac

from google.appengine.ext import db

def users_key(group='default'):
    return db.Key.from_path('users', group)

class User(db.Model):
    username = db.StringProperty(required = True)
    email = db.StringProperty(required = True)
    password_hash = db.StringProperty(required = True)

    def gravatar(self, size):
        # create hash for gravatar
        email_hash = hashlib.md5(self.email.lower()).hexdigest()
        # construct the url
        gravatar_url = "https://www.gravatar.com/avatar/%s?s=%d" % (email_hash, size)
        return gravatar_url

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid, parent=users_key())

    @classmethod
    def by_name(cls, username):
        user = User.all().filter('username =', username).get()
        return user

    @classmethod
    def register(cls, username, password, email=None):
        password_hash = make_password_hash(username, password)
        return User(parent=users_key(),username=username, email=email, password_hash=password_hash)

    @classmethod
    def login(cls, username, password):
        user = cls.by_name(username)
        if user and valid_password(username, password, user.password_hash):
            return user


# Hashing Functions
def make_salt():
    return ''.join(random.choice(string.letters) for x in range(5))

def make_password_hash(username, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(username + pw + salt).hexdigest()
    return '%s|%s' % (h, salt)

def valid_password(username, pw, h):
    salt = h.split("|")[1]
    if h == make_password_hash(username, pw, salt):
        return True
