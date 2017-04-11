from app.handlers.base import BlogHandler


class UserPage(BlogHandler):
    def get(self):
        if self.user:
            p = self.user.posts.get()
            if p is not None:
                posts = self.user.posts
            else:
                posts = None

            self.render('welcome.html', logged_in=self.logged_in, user = self.user, posts=posts)
        else:
            self.redirect('/signup')
