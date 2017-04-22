from app.handlers.base import BlogHandler
from app.models import Post

class EditPostPage(BlogHandler):
    def get(self, post_id):
        if not self.user:
            error = "You must be logged in to edit a post."
            self.redirect("/login?error=" + error)

        post = Post.by_id(int(post_id))
        if post.author.username == self.user.username:
            self.render("edit_post.html",
                        logged_in=self.logged_in,
                        post=post)
        else:
            error = "You must be the owner of the post to edit it."
            self.redirect('/blog/post/%s?error=%s' % (post_id, error))




    def post(self, post_id):
        if not self.user:
            error = "You must be logged in to edit a post."
            self.redirect('/login?error=' + error)

        subject = self.request.get("subject")
        content = self.request.get('content')

        post = Post.edit(id=int(post_id),
                         subject=subject,
                         content=content,
                         user=self.user)

        if post:
            success_message = "Blog post was successfully updated."
            self.redirect("/blog/post/%s?success=%s" % (post_id, success_message))
        else:
            self.render("edit_post.html",
                        logged_in=self.logged_in,
                        subject=post.subject,
                        content=post.content,
                        error="Something went wrong, please try again.")
