from app.handlers.base import BlogHandler
from app.models import Post

class BlogFrontPage(BlogHandler):
    def get(self):
        posts = Post.recent_posts(10)
        self.render("blog.html", logged_in=self.logged_in, posts=posts)
