import webapp2

from app.handlers import HomePage, SignupPage, LoginPage, UserPage, UserSettingsPage, LogoutHandler, BlogFrontPage, NewPostPage, PostPage, EditPostPage, DeletePostHandler, PostCommentHandler, LikePost, UnlikePost


app = webapp2.WSGIApplication([
    (r'/', HomePage),
    (r'/user', UserPage),
    (r'/user/settings', UserSettingsPage),
    (r'/signup', SignupPage),
    (r'/login', LoginPage),
    (r'/logout', LogoutHandler),
    (r'/blog', BlogFrontPage),
    (r'/blog/post/new', NewPostPage),
    (r'/blog/post/(\d+)', PostPage),
    (r'/blog/post/(\d+)/like', LikePost),
    (r'/blog/post/(\d+)/unlike', UnlikePost),
    (r'/blog/post/(\d+)/comment', PostCommentHandler),
    (r'/blog/post/(\d+)/edit', EditPostPage),
    (r'/blog/post/(\d+)/delete', DeletePostHandler)

], debug=True)
