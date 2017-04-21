import time
from google.appengine.ext import db
from user import User
from post import Post

class Like(db.Model):
    post = db.ReferenceProperty(Post,
                                  collection_name='likes',
                                  required=True)
    created = db.DateTimeProperty(auto_now_add = True)
    user = db.ReferenceProperty(User,
                                  collection_name='likes',
                                  required=True)


    @classmethod
    def by_id(cls, uid):
        return Like.get_by_id(uid)
    
    @classmethod
    def delete(cls, id):
        like = Like.by_id(int(id))
        if like:
            db.delete(like)
            time.sleep(0.2)
            return True
        return False
