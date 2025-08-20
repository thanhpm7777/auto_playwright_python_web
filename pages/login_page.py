import allure
from playwright.sync_api import expect
from .base_page import BasePage


class LoginPage(BasePage):
    SIGN_IN_LINK = "Đăng nhập"  # text của link
    BTN_SIGN_IN = "ĐĂNG NHẬP"

    PH_EMAIL = "Tên đăng nhập hoặc email"
    PH_PASSWORD = "Mật khẩu"

    def goto(self):
        with allure.step("Mở trang chủ"):
            self.open()
        with allure.step("Đi tới trang Sign in"):
            self.click_nav(self.SIGN_IN_LINK)
        return self

    def login(self, email: str, password: str):
        with allure.step("Nhập thông tin đăng nhập"):
            self.fill_by_placeholder(self.PH_EMAIL, email)
            self.fill_by_placeholder(self.PH_PASSWORD, password)
        with allure.step("Đăng nhập"):
            self.click_button(self.BTN_SIGN_IN)
        return self

    # def assert_logged_in(self):
    #     with allure.step("Xác minh đã đăng nhập co username"):
    #         expect(self.page.get_by_role("link", name="thanhpm", exact=True)).to_be_visible()

    def assert_logged_in(self):
        with allure.step("Xác minh đã đăng nhập có username"):
            expect(self.page.locator(".username")).to_have_text("thanhpm")


