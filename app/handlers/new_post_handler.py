from app.handlers.base import BlogHandler
from app.models import Post

class NewPostPage(BlogHandler):
    def get(self):
        if self.user:
            self.render("new_post.html", logged_in=self.logged_in)
        else:
            self.redirect("/login")

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get('content')
        author = self.user
        print(author)
        if subject and content:
            p = Post(subject=subject, content=content, author=author)
            p_key = p.put()
            self.redirect("/blog/post/%d" % p_key.id())
        else:
            error = "we need both a subject and the content"
            self.render("new_entry.html", subject=subject, content=content, error=error)
