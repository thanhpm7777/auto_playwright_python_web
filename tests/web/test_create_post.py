import allure
from faker import Faker
from core.utils import now_slug
from pages.post_editor_page import PostEditorPage
from pages.login_page import LoginPage
from core.config import settings
import pytest
fake = Faker()

@pytest.mark.smoke
@allure.feature("Post")
@allure.severity(allure.severity_level.CRITICAL)
class TestCreatePost:
    @allure.story("Tạo bài viết mới thành công")
    @allure.tag("auth")
    def test_create_post_success(self, page):
        lp = LoginPage(page)
        lp.goto().login(settings.USER_EMAIL, settings.USER_PASSWORD).assert_logged_in("test1111")
        pe = PostEditorPage(page)


        #pe.open().goto_editor().create_post(title, about, body, tags).assert_post_published(title)
        pe.open().goto_editor()
        pe.create_post("abcd", "15", "1234")