import os
# import re

import jinja2
import webapp2

import hmac

from app.models.user import User

template_dir = os.path.join(os.path.dirname(__file__), '../templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

SECRET = "3Kc%lCme0s.4CLemC94.SS9mlEd84.4295890"

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(SECRET, val).hexdigest())

def check_secure_val(secure_val):
    val = secure_val.split("|")[0]
    if secure_val == make_secure_val(val):
        return val

class BlogHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def set_secure_cookie(self, name, val):
        cookie_val = str(make_secure_val(val))
        self.response.headers.add_header('Set-Cookie', '%s=%s; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)

    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    # for handling Alerts, trying to find a better place for this
    def message_builder(self):
        # checks if there is a message to display
        error = self.request.get('error')
        success = self.request.get('success')
        message = {}

        if error:
            message['display'] = 'danger'
            message['message'] = error
        if success:
            message['display'] = 'success'
            message['message'] = success

        return message

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        # on every page render we check if there is an alert
        # message to display and builds alert object
        self.message = self.message_builder()


        self.logged_in = False
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))
        if self.user:
            self.logged_in = True
        else:
            self.logged_in = False
