import pytest
import allure
from core.config import settings
from core.allure_helpers import attach_page_screenshot
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    """
    Launch 1 browser cho cả session.
    """
    with sync_playwright() as p:
        browser_type = getattr(p, settings.PW_BROWSER)  # chromium | firefox | webkit
        print(f">>> Launching {settings.PW_BROWSER} | headless={settings.PW_HEADLESS}")
        browser = browser_type.launch(headless=settings.PW_HEADLESS)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser, request):
    """
    Tạo context & page cho từng test.
    """
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(settings.PW_TIMEOUT)
    yield page

    rep = getattr(request.node, "rep_call", None)
    if rep and rep.failed:
        with allure.step("Đính kèm screenshot khi lỗi"):
            attach_page_screenshot(page, name=f"failed-{request.node.name}")
    context.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
