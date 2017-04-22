import time
from google.appengine.ext import db
from app.models.user import User
from app.models.post import Post

class Like(db.Model):
    post = db.ReferenceProperty(Post,
                                collection_name='likes',
                                required=True)
    created = db.DateTimeProperty(auto_now_add = True)
    user = db.ReferenceProperty(User,
                                collection_name='likes',
                                required=True)


    @classmethod
    def by_id(cls, lid):
        return Like.get_by_id(lid)

    @classmethod
    def delete(cls, lid):
        like = Like.by_id(int(lid))
        if like:
            db.delete(like)
            time.sleep(0.2)
            return True
        return False
