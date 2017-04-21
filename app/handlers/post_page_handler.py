from app.models import Post
from app.handlers.base import BlogHandler

class PostPage(BlogHandler):
    def get(self, post_id):
        post = Post.by_id(int(post_id))
        comments = post.get_comments()

        can_edit = False
        if not post:
            self.error(404)
            return
        if self.user and post.author.username == self.user.username:
            can_edit = True
        self.render("single_post.html",user=self.user, logged_in=self.logged_in, comments=comments, post=post, can_edit=can_edit, message=self.message)
