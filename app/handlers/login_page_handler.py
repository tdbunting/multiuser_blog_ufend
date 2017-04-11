from app.handlers.base import BlogHandler
from app.models import User

class LoginPage(BlogHandler):
    def get(self):
        if self.user:
            self.redirect("/user")
        else:
            self.render("user_login_form.html")

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")

        user = User.login(username, password)
        if user:
            self.login(user)
            self.redirect('/user')
        else:
            msg = 'Invalid Username or Password'
            self.render("user_login_form.html", error=msg)
