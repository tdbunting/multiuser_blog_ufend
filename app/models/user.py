import random
import string
import urllib
import hashlib
import hmac

from google.appengine.ext import db
# from google.appengine.api import search

def users_key(group='default'):
    return db.Key.from_path('users', group)

class User(db.Model):
    username = db.StringProperty(required = True)
    email = db.StringProperty(required = True)
    password_hash = db.StringProperty(required = True)

    #social media links
    facebook_username = db.StringProperty()
    twitter_username = db.StringProperty()
    github_username = db.StringProperty()
    instagram_username = db.StringProperty()

    def gravatar(self, size):
        # create hash for gravatar
        email_hash = hashlib.md5(self.email.lower()).hexdigest()
        # construct the url
        gravatar_url = "https://www.gravatar.com/avatar/%s?s=%d" % (email_hash, size)
        return gravatar_url

    def facebook_link(self):
        return "https://www.facebook.com/%s" % self.facebook_username

    def twitter_link(self):
        return "https://twitter.com/%s" % self.twitter_link

    def instagram_link(self):
        return "https://www.instagram.com/%s" % self.instagram_username

    def github_link(self):
        return "https://github.com%s" % self.github_username


    #TODO: FIGURE OUT BETTER WAY OF LIKING
    def has_liked_post(self, post_key):
        like = self.likes.filter("post =", post_key)

        if like.count() == 0:
            return False
        else:
            # print(like[0])
            return True

    def has_liked_post_returns_like(self, post_key):
        like = self.likes.filter("post =", post_key)

        if like.count() == 0:
            return False
        else:
            print(True)
            return like[0].key().id()

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
