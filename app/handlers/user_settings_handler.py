from app.handlers.base import BlogHandler


# TODO: One day I will implement updating user info.. that day is not today

class UserSettingsPage(BlogHandler):
    def get(self):
        if self.user:
            self.render('user_settings_page.html', logged_in=self.logged_in, user=self.user)
        else:
            self.redirect('/login')

    # def post(self):
    #     if self.user:
    #         user = self.user
    #         user.edit()
