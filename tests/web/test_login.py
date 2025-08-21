import allure
from core.config import settings
from pages.login_page import LoginPage
import pytest


@pytest.mark.smoke
@allure.feature("Authentication")
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin:
    @allure.story("Login thành công")
    def test_login_success(self, page):
        lp = LoginPage(page)
        lp.goto().login(settings.USER_EMAIL, settings.USER_PASSWORD).assert_logged_in("test1111")

    
    @allure.story("Login không thành công")
    def test_login_fail(self, page):
        lp= LoginPage(page)
        lp.goto().login(settings.USER_EMAIL, "pasw")
        lp.assert_login_fail("Thông tin tài khoản hoặc mật khẩu không đúng.")