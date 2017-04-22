from app.handlers.base import BlogHandler
from app.models.comment import Comment
from app.models.post import Post

import time

class PostCommentHandler(BlogHandler):
    def post(self, post_id):
        if not self.user:
            self.redirect("/login")
        post = Post.by_id(int(post_id))
        comment = self.request.get("comment")
        user = self.user
        
        if post and comment and user:
            comment = Comment(post=post, comment=comment, user=user)
            comment.put()
            time.sleep(0.2)
            self.redirect("/blog/post/" + post_id)
        else:
            error = "Cannot post an empty comment"
            self.redirect("/blog/post/%d?error=%s" % (int(post_id), error))
