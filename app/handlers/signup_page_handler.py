import re

from app.models import User
from app.handlers.base import BlogHandler

# REGULAR EXPRESSIONS
USER_REX = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
EMAIL_REX = re.compile(r"^[\S]+@[\S]+.[\S]+$")
PASSWORD_REX = re.compile(r"^.{3,20}$")


class Register(BlogHandler):
    def get(self):
        if self.user:
            self.redirect("/user")
        else:
            self.render("user_sign_up_form.html", error="")

    def post(self):
        err = False
        self.username = self.request.get('username')
        self.email = self.request.get('email')
        self.password = self.request.get('password')
        self.password_verification = self.request.get('verify')

        params = dict(username = self.username, email = self.email)
        if not verify_username(self.username):
            params['error_username'] = "Not a valid Username"
            err = True
        if not verify_email(self.email):
            params['error_email'] = "Not a valid Email"
            err = True
        if not verify_password(self.password):
            params['error_password'] = "Not a valid Password"
            err = True
        if not verify_verification(self.password, self.password_verification):
            params['error_verify'] = "Passwords do not match"
            err = True

        if not err:
            self.done()
        else:
            self.render("user_sign_up_form.html", **params)

    def done(self, *a, **kw):
        raise NotImplementedError

class SignupPage(Register):
    def done(self):
        user = User.by_name(self.username)
        if user:
            msg = "Username Already Exists"
            self.render('user_sign_up_form.html', error_username=msg)
        else:
            user = User.register(self.username, self.password, self.email)
            user.put()

            self.login(user)
            self.redirect('/user')
        # logging.debug(user)


# Validation Functions

def verify_username(username):
    if USER_REX.match(username):
        return username
    else:
        return False

def verify_email(email):
    if EMAIL_REX.match(email):
        return email
    else:
        return False

def verify_password(password):
    if PASSWORD_REX.match(password):
        return password
    else:
        return False

def verify_verification(password, password_verification):
    if password == password_verification:
        return True
    else:
        return False
