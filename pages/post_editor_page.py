import allure
from playwright.sync_api import expect
from .base_page import BasePage


class PostEditorPage(BasePage):
    LINK_NEW_ARTICLE = "New Article"

    PH_TITLE = "Article Title"
    PH_ABOUT = "What's this article about?"
    PH_BODY = "Write your article (in markdown)"
    PH_TAGS = "Enter tags"

    BTN_PUBLISH = "Publish Article"

    def goto_editor(self):
        with allure.step("Mở form tạo bài viết"):
            self.click_nav(self.LINK_NEW_ARTICLE)
        return self

    def create_post(self, title: str, about: str, body: str, tags: str):
        with allure.step("Nhập nội dung bài viết"):
            self.fill_by_placeholder(self.PH_TITLE, title)
            self.fill_by_placeholder(self.PH_ABOUT, about)
            self.fill_by_placeholder(self.PH_BODY, body)
            self.fill_by_placeholder(self.PH_TAGS, tags)
        with allure.step("Xuất bản bài viết"):
            self.click_button(self.BTN_PUBLISH)
        return self

    def assert_post_published(self, title: str):
        with allure.step("Xác minh tiêu đề bài viết hiển thị"):
            expect(self.page.get_by_role("heading", name=title, level=1)).to_be_visible()