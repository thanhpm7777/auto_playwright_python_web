import os
import json
import allure
import pytest
from core.config import settings
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def auth_storage_state(browser):
    """
    Đăng nhập 1 lần ở scope=Session, lưu storage_state cho các test khác dùng lại.
    Nếu file đã tồn tại -> bỏ qua.
    """
    storage_path = settings.STORAGE_STATE
    os.makedirs(os.path.dirname(storage_path), exist_ok=True)

    if os.path.exists(storage_path):
        return storage_path

    context = browser.new_context()
    page = context.new_page()

    with allure.step("Đăng nhập 1 lần và lưu storage_state"):
        lp = LoginPage(page)
        lp.goto().login(settings.USER_EMAIL, settings.USER_PASSWORD).assert_logged_in()
        context.storage_state(path=storage_path)

    context.close()
    return storage_path


@pytest.fixture()
def page_authenticated(browser, auth_storage_state):
    context = browser.new_context(storage_state=auth_storage_state)
    page = context.new_page()
    yield page
    context.close()