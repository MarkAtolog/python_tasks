from api_testing.models.post import Post
from api_testing.models.user import User
from framework.api.api_util import ApiUtil
from api_testing.constants.endpoints import Endpoints
from framework.logger.logger import Logger


class ApiSteps:
    @staticmethod
    def get_all_posts():
        Logger().logger.info("Trying to get all posts")
        return ApiUtil.get(url=Endpoints.get_posts, model=Post)

    @staticmethod
    def get_post(post_id: int):
        Logger().logger.info(f"Trying to get post with id = {post_id}")
        return ApiUtil.get(url=Endpoints.get_post.format(post_id), model=Post)

    @staticmethod
    def send_new_post(new_post: Post):
        Logger().logger.info("Trying to send new post")
        return ApiUtil.post(url=Endpoints.get_posts, data=new_post, model=Post)

    @staticmethod
    def get_all_users():
        Logger().logger.info("Trying to get all users")
        return ApiUtil.get(url=Endpoints.get_users, model=User)

    @staticmethod
    def get_user(user_id: int):
        Logger().logger.info("Trying to get all users")
        return ApiUtil.get(url=Endpoints.get_user.format(user_id), model=User)
