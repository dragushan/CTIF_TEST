import pytest


@pytest.mark.usefixtures("init_driver")

class TestDummy():
    def test_dummy_func(self):
        print("I`m dummy test line 1")
        print("I`m dummy test line 2")
        import pdb; pdb.set_trace()


