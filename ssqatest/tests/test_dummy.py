import pytest




@pytest.mark.usefixtures("init_driver")

class TestDummy():
    def test_dummy_func(self):
        print("I`m dummy test line 1")
        self.driver.get("https://www.google.com/")
        import pdb; pdb.set_trace()


