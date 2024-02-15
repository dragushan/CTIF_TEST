import pdb

import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut

@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):

        my_account_o = MyAccountSignedOut(self.driver)
        #go to my acc
        my_account_o.go_to_my_account()

        #fill in email
        my_account_o.input_register_email("eeeqqqeee@ghjk.vbn")
        my_account_o.input_register_password("dszfdxgfcgvhb123456WER")
        my_account_o.click_register_button()
        pdb.set_trace()

        #fill in password
        #click register
        #verify user is registered