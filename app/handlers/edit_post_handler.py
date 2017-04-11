from app.handlers.base import BlogHandler
from app.models import Post

class EditPostPage(BlogHandler):
    def get(self, post_id):
        if self.user and post_id:
            post = Post.by_id(int(post_id))
            if post.author.username == self.user.username:
                self.render("edit_post.html",
                            logged_in=self.logged_in,
                            post=post)
            else:
                self.redirect('/blog/post/%d' % post_id)
        else:
            self.redirect("/login")


    def post(self, post_id):
        subject = self.request.get("subject")
        content = self.request.get('content')

        post = Post.edit(id=int(post_id),
                  subject = subject,
                  content = content,
                  user = self.user)

        if post:
            self.redirect("/blog/post/" + post_id)
        else:
            self.render("edit_post.html",
                        logged_in=self.logged_in,
                        subject=post.subject,
                        content=post.content)
