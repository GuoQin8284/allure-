import os

import pytest

from base.base_analyze import Analyze
from base.base_driver import baseDriver
from page.page_add_contact import AddContact
from page.page_contact import ContactList
from page.sava_contact import SaveContact


class TestContact():

    def setup(self):
        self.driver = baseDriver(appPackage="com.android.contacts", appActivity="com.android.contacts.activities.PeopleActivity")
        self.pageContact = ContactList(self.driver)
        self.page_add_contact = AddContact(self.driver)
        self.saveContact = SaveContact(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", Analyze(fileName="data_contact.yaml", className="TestContact"))
    def test_add_contact(self,args):
        contact_text = args["contact_text"]
        phone = args["phone"]
        self.pageContact.click_new_contact()
        # 判断当前是否出现保存提示
        if self.page_add_contact.is_toast():
            self.page_add_contact.click_local_save()
        self.page_add_contact.input_contact(contact_text)
        self.page_add_contact.input_phone(phone)
        # 返回保存
        self.page_add_contact.press_keyCode(4)
        assert contact_text == self.saveContact.get_contact_tittl()
        assert phone == self.saveContact.get_contact_phone()