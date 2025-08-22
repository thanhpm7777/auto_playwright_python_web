import allure
from playwright.sync_api import expect
from .base_page import BasePage


class PostEditorPage(BasePage):
    LINK_NEW_ARTICLE = "user-avatar"
    lbl_setting = "Cài đặt thông tin"
    lbl_dangbai = "Đăng bài"

    PH_TITLE = "title"
    PH_category = "#category_id"
    PH_BODY = "presentation"
    PH_TAGS = "Enter tags"

    BTN_PUBLISH = "Publish Article"

    def goto_editor(self):
        with allure.step("Mở form tạo bài viết"):
            self.get_by_class(self.LINK_NEW_ARTICLE).click()
            self.click_nav(self.lbl_setting)
            self.click_link_or_button(self.lbl_dangbai, expect_nav=True)
        return self

    def create_post(self, title, category,body):
        with allure.step("Nhập nội dung bài viết"):
            self.fill_by_name(self.PH_TITLE, title)
            self.select_by_value(self.PH_category, category)
            #self.fill_by_placeholder(self.PH_BODY, body)
            # self.fill_by_placeholder(self.PH_TAGS, tags)
       # with allure.step("Xuất bản bài viết"):
            #self.click_button(self.BTN_PUBLISH)
        return self

    def assert_post_published(self, title: str):
        with allure.step("Xác minh tiêu đề bài viết hiển thị"):
            expect(self.page.get_by_role("heading", name=title, level=1)).to_be_visible()