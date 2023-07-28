import string
import time
from random import choice
import pytest
from re import sub
import copy


class TestHomePage:
    """Test class for Homepage"""

    @pytest.fixture(scope='class')
    def resources(self, logger, config, browser, log_as_admin):
        pass
        # SetUp class action

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, resources):
        resources.pages.homepage_page.open_page()
        yield

    def test_add_dashboard(self, resources):
        """
        Test the Dashboard add in Homepage

        """
        pass

    def test_edit_dashboard(self, resources):
        """
        Test the Dashboard editing in Homepage

        """
        pass

    def test_remove_one_dashboard(self, resources):
        """
        Test the Dashboard removing in Homepage

        """
        pass
    
    def test_add_widget(self, resources):
        """
        Test the widget adding in Homepage

        """
        pass

    def test_edit_widget(self, resources):
        """
        Test the widget editing in Homepage

        """
        pass

    def test_remove_widget(self, resources):
        """
        Test the widget removing in Homepage


        """
        pass

    def test_set_chart_value(self, resources):
        """
        Test for setting values on widget

        """
        pass

    def test_data_visibility_on_chart(self, resources):
        """
        Test if values are or are not displayed on chart with manual y_axis min/max depends on provided limits
            
        """
        pass
    