import allure
from allure_commons.types import AttachmentType


def attach_page_screenshot(page, name: str = "screenshot"):
    try:
        png = page.screenshot(full_page=True)
        allure.attach(png, name=name, attachment_type=AttachmentType.PNG)
    except Exception as e:
        allure.attach(str(e), name=f"{name}-error", attachment_type=AttachmentType.TEXT)