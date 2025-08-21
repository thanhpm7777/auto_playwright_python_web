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


        # ===== Thêm helper locator dạng khác =====

    # Lấy theo CSS selector
    def get_by_css(self, selector: str):
        return self.page.locator(selector)

    # Lấy theo ID
    def get_by_id(self, element_id: str):
        return self.page.locator(f"#{element_id}")

    # Lấy theo class name
    def get_by_class(self, class_name: str):
        return self.page.locator(f".{class_name}")

    # Lấy theo text (thường dùng cho label hoặc button có text rõ ràng)
    def get_by_text(self, text: str, exact: bool = True):
        return self.page.get_by_text(text, exact=exact)

    # Lấy theo name attribute (input name, select name)
    def get_by_name(self, name: str):
        return self.page.locator(f"[name='{name}']")

    # Lấy theo XPath (ít dùng nhưng vẫn cần khi CSS khó)
    def get_by_xpath(self, xpath: str):
        return self.page.locator(f"xpath={xpath}")

    # Click theo text (shortcut)
    def click_by_text(self, text: str, exact: bool = True):
        self.get_by_text(text, exact).click()

    # Điền input theo name
    def fill_by_name(self, name: str, value: str):
        self.get_by_name(name).fill(value)