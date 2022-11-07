from api_testing.models.address import Address
from api_testing.models.company import Company
from api_testing.models.geo import Geo
from api_testing.models.post import Post
from api_testing.models.user import User
from api_testing.steps.api_steps import ApiSteps
from framework.common.string_utils import StringUtils


class TestApi:
    def test_jsonplaceholder(self):
        expected_status_code = 200
        expected_content_type = "application/json"

        all_posts_response = ApiSteps.get_all_posts()

        assert all_posts_response.status_code == expected_status_code, \
            f"Wrong response status code. Expected: '{expected_status_code}'. " \
            f"Actual: '{all_posts_response.status_code}'"
        assert all_posts_response.headers["Content-Type"].find(expected_content_type) >= 0, \
            f"Wrong response content type. Expected: '{expected_content_type}'. " \
            f"Actual: \'{all_posts_response.headers['Content-Type']}\'"

        sorted_list = sorted(all_posts_response.model, key=lambda x: x.id)
        assert all_posts_response.model == sorted_list, "Response content is unordered"

        expected_post = Post(id=99, user_id=10)

        one_post_response = ApiSteps.get_post(expected_post.id)

        assert one_post_response.status_code == expected_status_code, \
            f"Wrong response status code. Expected: '{expected_status_code}'. " \
            f"Actual: '{all_posts_response.status_code}'"

        assert one_post_response.model.id == expected_post.id, \
            f"Posts' id doesn't match. Expected: '{expected_post.id}'. " \
            f"Actual: '{one_post_response.model.id}'"
        assert one_post_response.model.user_id == expected_post.user_id, \
            f"Posts' User id doesn't match. Expected: '{expected_post.user_id}'. " \
            f"Actual: '{one_post_response.model.user_id}'"
        assert one_post_response.model.title is not None and one_post_response.model.title != "", \
            "Post title is empty"
        assert one_post_response.model.body is not None and one_post_response.model.body != "", \
            "Post body is empty"

        wrong_post_expected_status_code = 404
        wrong_post = Post(id=150)

        wrong_post_response = ApiSteps.get_post(wrong_post.id)

        assert wrong_post_response.status_code == wrong_post_expected_status_code, \
            f"Wrong response status code. Expected: '{wrong_post_expected_status_code}'. " \
            f"Actual: '{wrong_post_response.status_code}'"
        assert wrong_post_response.content == "{}", "Response body is not empty"

        new_post = Post(user_id=1,
                        title=StringUtils.get_random_string(),
                        body=StringUtils.get_random_string())
        new_post_expected_status_code = 201

        new_post_response = ApiSteps.send_new_post(new_post)

        assert new_post_response.status_code == new_post_expected_status_code, \
            f"Wrong response status code. Expected: '{new_post_expected_status_code}'. " \
            f"Actual: '{new_post_response.status_code}'"
        assert new_post_response.model.title == new_post.title, \
            f"Title doesn't match. Expected: '{new_post.title}'. " \
            f"Actual: '{new_post_response.model.title}'"
        assert new_post_response.model.body == new_post.body, \
            f"Post body doesn't match. Expected: '{new_post.body}'. " \
            f"Actual: '{new_post_response.model.body}'"
        assert new_post_response.model.user_id == new_post.user_id, \
            f"Posts' User id doesn't match. Expected: '{new_post.user_id}'. " \
            f"Actual: '{new_post_response.model.user_id}'"
        assert new_post_response.model.id is not None, "Post id is not presented in response body"

        test_user = User(id=5,
                         name="Chelsey Dietrich",
                         username="Kamren",
                         email="Lucio_Hettinger@annie.ca",
                         address=Address(street="Skiles Walks",
                                         suite="Suite 351",
                                         city="Roscoeview",
                                         zipcode="33263",
                                         geo=Geo(lat="-31.8129",
                                                 lng="62.5342")),
                         phone="(254)954-1289",
                         website="demarco.info",
                         company=Company(name="Keebler LLC",
                                         catch_phrase="User-centric fault-tolerant solution",
                                         bs="revolutionize end-to-end systems"))

        all_users_response = ApiSteps.get_all_users()

        assert all_users_response.status_code == expected_status_code, \
            f"Wrong response status code. Expected: '{expected_status_code}'. " \
            f"Actual: '{all_users_response.status_code}'"
        assert all_users_response.headers["Content-Type"].find(expected_content_type) >= 0, \
            f"Wrong response content type. Expected: '{expected_content_type}'. " \
            f"Actual: \'{all_users_response.headers['Content-Type']}\'"
        assert next(filter(lambda x: x.id == 5, all_users_response.model)) == test_user, \
            "Users are not equal"

        get_user_response = ApiSteps.get_user(test_user.id)

        assert get_user_response.model == test_user, "Users are not equal"
