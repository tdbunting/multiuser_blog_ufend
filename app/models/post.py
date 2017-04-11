import time
from google.appengine.ext import db
from user import User

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    author = db.ReferenceProperty(User,
                                  collection_name='posts',
                                  required=True)
    def snippet(self):
        if len(self.content) < 120:
            return self.content

        return self.content[0:120] + "..."

    @classmethod
    def by_id(cls, uid):
        print(int(uid))
        return Post.get_by_id(uid)


    @classmethod
    def recent_posts(cls, max_posts=10):
        return db.GqlQuery("SELECT * FROM Post ORDER BY created DESC LIMIT %d" % max_posts)

    @classmethod
    def edit(cls, id, subject, content, user):
        post = Post.by_id(id)
        if post and user.username == post.author.username:
            post.subject = subject
            post.content = content
            post.put()
            return True

        return False

    @classmethod
    def delete(cls, id, user):
        post = Post.by_id(int(id))
        if post and user.username == post.author.username:
            db.delete(post)
            time.sleep(0.2)
            return True
        return False
