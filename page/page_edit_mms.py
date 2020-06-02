import allure
from selenium.webdriver.common.by import By

from base.base_action import Action


class EditMms(Action):
    # 接收者输入框
    recipient_edit_text = By.ID, "com.android.mms:id/recipients_editor"
    mms_edit_text = By.ID, "com.android.mms:id/embedded_text_editor"
    send_button = By.ID, "com.android.mms:id/send_button_sms"

    # 输入联系人
    @allure.step(title="输入短信接收人")
    def input_recipienter(self, text):
        self.input_text(self.recipient_edit_text, text)

    @allure.step(title="输入短信内容")
    def input_mms_text(self,text):
        self.input_text(self.mms_edit_text, text)

    @allure.step(title="点击发送按钮，发送短信")
    def click_send(self):
        self.click(self.send_button)