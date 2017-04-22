from app.handlers.base import BlogHandler
from app.models import Post

class DeletePostHandler(BlogHandler):
    def post(self, post_id):
        if self.user:
            post = Post.delete(id=int(post_id), user=self.user)
            if post:
                message = "Post deleted successfully"
                self.redirect("/user?success=%s" % message)
            else:
                self.render("/blog/post/" + post_id,
                            logged_in=self.logged_in,
                            subject = post.subject,
                            content = post.content)
        else:
            message = "You must be logged in to delete a post."
            self.redirect('/login?error=%s' % message)
