# import allure
# from faker import Faker
# from core.utils import now_slug
# from pages.post_editor_page import PostEditorPage
#
# fake = Faker()
#
#
# @allure.feature("Post")
# @allure.severity(allure.severity_level.CRITICAL)
# class TestCreatePost:
#     @allure.story("Tạo bài viết mới thành công")
#     @allure.tag("auth")
#     def test_create_post_success(self, page_authenticated):
#         page = page_authenticated
#         pe = PostEditorPage(page)
#
#         title = now_slug("how-to-playwright")
#         about = fake.sentence(nb_words=6)
#         body = "\n\n".join(fake.paragraphs(nb=3))
#         tags = "playwright,python,e2e"
#
#         pe.open().goto_editor().create_post(title, about, body, tags).assert_post_published(title)