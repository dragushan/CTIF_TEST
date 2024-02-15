import pdb

import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    @pytest.mark.tcid12
    def test_login_non_existing_user(self):
        print("******")
        print("TEST LOGIN EXISTING")
        print("******")
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username("user_1")
        my_account.input_login_password("my_password123")
        my_account.click_login_button()
        # pdb.set_trace()
        #error message
        expected_err = "Error: The username user_1 is not registered on this site. If you are unsure of your username, try your email address instead."
        my_account.wait_until_error_is_displayed(expected_err)

