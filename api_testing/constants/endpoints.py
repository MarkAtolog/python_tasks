from configuration.config_manager import ConfigManager


class Endpoints:
    __base_url = ConfigManager.config("url")
    get_posts = __base_url + "/posts"
    get_users = __base_url + "/users"
    get_user = __base_url + "/users/{}"
    get_post = __base_url + "/posts/{}"
