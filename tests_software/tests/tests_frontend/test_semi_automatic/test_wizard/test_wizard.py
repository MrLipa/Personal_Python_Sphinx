import time
import pytest


class TestWizard:
    """Test class for Wizard."""

    @pytest.fixture(scope='class')
    def test_resources(self, logger, config, browser, log_as_admin):
        """Test set credentials during first login when the default password is <admin>.
        Be aware that the test will be failed when the password won't be <admin> and the Wizard won't appeared."""
        pass

    @pytest.mark.order(3)
    def test_set_credentials_at_first_login(self, resources):
        """Test set credentials during first login when the default password is <admin>.
        Be aware that the test will be failed when the password won't be <admin> and the Wizard won't appeared."""
        time.sleep(5)

    @pytest.mark.parametrize("ds",[1,1,1])
    def test_wizard5(ds):
        """This function does nothing."""
        pass

    @pytest.mark.skip("asdasd")
    def test_wizard3(ds):
        """This function does nothing."""
        pass

    def test_resources1():
        """This function does nothing."""
        pass


# import pytest


# def resources1():
#     """This function does nothing."""
#     pass

# @pytest.mark.parametrize("ds",[1,1,1])
# def test_wizard2(ds):
#     """This function does nothing."""
#     pass

# @pytest.mark.skip("asdasd")
# def test_wizard3(ds):
#     """This function does nothing."""
#     pass

# def resources4():
#     """This function does nothing."""
#     pass


# @pytest.mark.parametrize("ds",[1,1,1])
# def test_wizard5(ds):
#     """This function does nothing."""
#     pass