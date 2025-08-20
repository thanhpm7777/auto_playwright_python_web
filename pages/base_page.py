from playwright.sync_api import Page, expect
from core.config import settings


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(settings.PW_TIMEOUT)

    def open(self, path: str = ""):
        # BASE_URL có thể là URL có hash routing (#/)
        base = settings.BASE_URL
        if path:
            if base.endswith("/") and path.startswith("/"):
                url = base[:-1] + path
            else:
                url = base + path
        else:
            url = base
        self.page.goto(url)
        return self

    def assert_url_contains(self, text: str):
        expect(self.page).to_have_url(lambda url: text in url)

    def click_nav(self, name: str):
        self.page.get_by_role("link", name=name, exact=True).click()

    def fill_by_placeholder(self, placeholder: str, value: str):
        self.page.get_by_placeholder(placeholder).fill(value)

    def click_button(self, name: str):
        self.page.get_by_role("button", name=name, exact=True).click()