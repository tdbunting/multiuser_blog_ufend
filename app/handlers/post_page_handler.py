from app.models import Post
from app.handlers.base import BlogHandler

class PostPage(BlogHandler):
    def get(self, post_id):
        post = Post.by_id(int(post_id))
        can_edit = False

        print(post.author.username)

        if not post:
            self.error(404)
            return
        if post.author.username == self.user.username:
            can_edit = True
        self.render("single_post.html", logged_in=self.logged_in, post=post, can_edit=can_edit)
