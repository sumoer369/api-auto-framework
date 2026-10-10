from utils.request_util import RequestUtil

class LoginApi:
    def __init__(self):
        self.req = RequestUtil()

    def get_post(self, post_id):
        return self.req.get(f"/posts/{post_id}")

    def get_all_posts(self):
        return self.req.get("/posts")