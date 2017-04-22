from app.handlers.base import BlogHandler
from app.models import Post

class NewPostPage(BlogHandler):
    def get(self):
        if self.user:
            self.render("new_post.html", logged_in=self.logged_in)
        else:
            message = "Must be logged in to create a blog post."
            self.redirect("/login?error=%s" % message)

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get('content')
        if self.user:
            author = self.user
            if subject and content:
                post = Post(subject=subject, content=content, author=author)
                post_key = post.put()
                message = "Post Created Successfully!"
                self.redirect("/blog/post/%d?success=%s" % (post_key.id(), message))
            else:
                error = "we need both a subject and the content"
                self.render("new_entry.html", subject=subject, content=content, error=error)
        else:
            error = "we need both a subject and the content"
            self.render("login.html", error=error)
