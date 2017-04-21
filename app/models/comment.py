from google.appengine.ext import db
from user import User
from post import Post

class Comment(db.Model):
    post = db.ReferenceProperty(Post,
                                  collection_name='comments',
                                  required=True)

    comment = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    user = db.ReferenceProperty(User,
                                  collection_name='comments',
                                  required=True)
