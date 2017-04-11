from app.handlers.base import BlogHandler

class HomePage(BlogHandler):
    def get(self):
        if self.user:
            self.redirect('/user')
        else:
            self.render('index.html', logged_in=self.logged_in)
