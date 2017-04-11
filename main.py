import webapp2

from app.handlers import HomePage, SignupPage, LoginPage, UserPage, LogoutHandler, BlogFrontPage, NewPostPage, PostPage, EditPostPage, DeletePostHandler


app = webapp2.WSGIApplication([
    (r'/', HomePage),
    (r'/user', UserPage),
    (r'/signup', SignupPage),
    (r'/login', LoginPage),
    (r'/logout', LogoutHandler),
    (r'/blog', BlogFrontPage),
    (r'/blog/post/new', NewPostPage),
    (r'/blog/post/(\d+)', PostPage),
    (r'/blog/post/(\d+)/edit', EditPostPage),
    (r'/blog/post/(\d+)/delete', DeletePostHandler)

], debug=True)
