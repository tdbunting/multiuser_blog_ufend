from app.handlers.base import BlogHandler
from app.models import Post

class DeletePostHandler(BlogHandler):
    def post(self, post_id):
        if self.user:
            post = Post.delete(id=int(post_id), user=self.user)
            if post:
                self.redirect("/blog")
            else:
                self.render("/blog/post/" + post_id,
                        logged_in=self.logged_in,
                        subject=post.subject,
                        content=post.content)
        else:
            self.redirect('/login')
