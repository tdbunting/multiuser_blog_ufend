import time
from app.handlers.base import BlogHandler
from app.models.post import Post
from app.models.like import Like

class LikeHandler(BlogHandler):
    def post(self, post_id):
        post_id = int(post_id)
        post = Post.by_id(post_id)

        # if the post doesnt exist no use in running anything else
        if not post:
            print("not a valid post")
            self.error(404)

        if self.user:
            # use post key to get like id from current user if one is available
            post_key = post.key()
            like_id = self.user.has_liked_post_returns_like(post_key)

            # if the user owns the current post they cannot like it
            if self.user.username == post.author.username:
                message="cannot like your own post"
                self.redirect("/blog/post/%d?error=%s" % (post_id, message))

            # if the user has already liked the post, we "unlike" the post
            elif like_id:
                delete_success = Like.delete(int(like_id))
                print(delete_success)
                if delete_success:
                    message = "Post unliked"
                    self.redirect("/blog/post/%d?success=%s" % (post_id, message))
                else:
                    message = "something went wrong unliking this post"
                    self.redirect("/blog/post/%d?error=%s" % (post_id, message))
                    print("unliking Now %s" % likes.count())

            # go ahead and like the post
            else:
                like = Like(user=self.user, post=post)
                message= "Post Liked"
                like.put()
                time.sleep(0.2)
                self.redirect('/blog/post/%d?success=%s' % (post_id, message))

        # cant like a post if you are not logged in
        else:
            message = "you must be logged in to like a post"
            self.redirect("/login?error=%s" % message)
