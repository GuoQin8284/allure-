import allure
from selenium.webdriver.common.by import By

from base.base_action import Action


class NewMmS(Action):
    new_mms_button = By.ID, "com.android.mms:id/action_compose_new"

    @allure.step(title="点击新建短信按钮")
    def click_new_mms(self):
        self.click(self.new_mms_button)