import pytest

from base.base_driver import baseDriver
from page.page_edit_mms import EditMms
from page.page_new_mms import NewMmS


class TestMms():

    def setup(self):
        self.driver = baseDriver(appPackage="com.android.mms", appActivity="com.android.mms.ui.ConversationList")
        self.newMms = NewMmS(self.driver)
        self.editMms = EditMms(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize(("recipienter", "text"),[(18871102549, "hello01"), (13545687895, "这是中国哈哈哈哈")])
    def test_sendMms(self, recipienter, text):
        self.newMms.click_new_mms()
        self.editMms.input_recipienter(recipienter)
        self.editMms.input_mms_text(text)
        self.editMms.click_send()