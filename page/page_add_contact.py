import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from base.base_action import Action


class AddContact(Action):
    get_toast = By.ID, "com.android.contacts:id/text"
    local_save = By.XPATH, "//*[@text='本地保存']"
    contact_edit_text = By.XPATH, "//*[@text='姓名']"
    phone_edit_text = By.XPATH, "//*[@text='电话']"

    @allure.step(title="判断是否有保存的toast提示")
    def is_toast(self):
        try:
            toast = self.find_element(feature=self.get_toast, timeout=2).text
            if toast:
                return True
        except TimeoutException:
            return False
    @allure.step(title="点击本地保存")
    def click_local_save(self):
        self.click(self.local_save)

    @allure.step(title="输入联系人")
    def input_contact(self, contact_text):
        self.input_text(self.contact_edit_text, contact_text)
        allure.attach(name="输入的联系人名称：", body=contact_text, attachment_type=allure.attachment_type.TEXT)
        allure.attach(name="截图", body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    @allure.step(title="输入电话号码")
    def input_phone(self, contact_phone):
        self.input_text(self.phone_edit_text, contact_phone)
        allure.attach(name="输入的电话号码：", body=contact_phone, attachment_type=allure.attachment_type.TEXT)
        allure.attach(name="截图", body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)