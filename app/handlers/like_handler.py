import time
from app.handlers.base import BlogHandler
from app.models.post import Post
from app.models.like import Like

class LikePost(BlogHandler):
    def post(self, post_id):
        post_id = int(post_id)
        post = Post.by_id(post_id)
        user = self.user
        print(user.has_liked_post(post))
        if not post:
            print("not a valid post")
            self.error(404)

        if user:
            if user.username == post.author.username:
                message="cannot like your own post"
                self.redirect("/blog/post/%d?error=%s" % (post_id, message))
            elif user.has_liked_post(post):
                message = "cannot like the same post twice"
                self.redirect("/blog/post%d?error=%s" %(post_id, message))
            else:
                like = Like(user=user, post=post)
                message= "Post Liked"
                like.put()
                time.sleep(0.2)
                self.redirect('/blog/post/%d?success=%s' % (post_id, message))
        else:
            message = "you must be logged in to like a post"
            self.redirect("/login?error=%s" % message)



class UnlikePost(BlogHandler):
    def post(self, post_id):
        post_id = int(post_id)
        post = Post.by_id(post_id)
        if self.user:
            if self.user.username == post.author.username:
                message="cannot like your own post"
                self.redirect("/blog/post/%d?error=%s" % (post_id, message))
            elif not self.user.has_liked_post(post):
                message="must like post before you can unlike it"
                self.redirect("/blog/post%d?error=%s" % (post_id, message))
            else:
                likes = post.likes.filter('user =', self.user.key())
                for like in likes:
                    did_delete = like.delete(like.key().id())
                    if did_delete:
                        message = "Post unliked"
                        self.redirect("/blog/post/%d?success=%s" % (post_id, message))
                    else:
                        message = "something went wrong unliking this post"
                        self.redirect("/blog/post/%d?error=%s" % (post_id, message))
                        print("unliking Now %s" % likes.count())
        else:
            message = "You must be logged in"
            self.redirect("/login?error=%s" % message)
