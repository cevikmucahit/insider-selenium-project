import time

from configs import init_driver
from configs.constants import RESULT_OUR_LOCATIONS_LIST, RESULT_DEPARTMENTS_LIST
from testCases.test_base import BaseTest
from pages.careersPage import CareersPage


class TestCareersPage(BaseTest):

    def test_01_check_locations_list(self):
        """
        Test method to check if the locations list on the Careers Page matches the expected list.

        Steps:
        1. Open the Careers Page.
        2. Scroll to the 'Our Locations' section.
        3. Retrieve the actual locations list from the page.
        4. Assert that the actual locations list is equal to the expected locations list.

        Parameters:
        - None

        Returns:
        - None
        """
        self.careersPage = CareersPage(self.driver)
        self.careersPage.open_careers_page()
        self.careersPage.close_cookie_warning()
        self.careersPage.scroll_to_our_location()
        time.sleep(0.7)

        actual_our_locations_list = []
        self.careersPage.add_locations_to_list(actual_our_locations_list)

        assert sorted(actual_our_locations_list) == RESULT_OUR_LOCATIONS_LIST

    def test_02_check_departments_list(self):
        """
        Test method to check if the departments list on the Careers Page matches the expected list.

        Steps:
        1. Scroll to the 'Departments' section.
        2. Click on the 'See All Teams' button.
        3. Retrieve the actual departments list from the page.
        4. Assert that the actual departments list is equal to the expected departments list.

        Parameters:
        - None

        Returns:
        - None
        """
        self.careersPage = CareersPage(self.driver)
        self.careersPage.scroll_to_departments()
        time.sleep(0.7)
        self.careersPage.click_see_all_teams_button()
        time.sleep(0.7)

        actual_departments_list = []
        self.careersPage.add_departments_to_list(actual_departments_list)

        assert sorted(actual_departments_list) == RESULT_DEPARTMENTS_LIST

    def test_03_check_life_at_insider(self):
        """
        Test method to check the presence of 'Life at Insider' section on the Careers Page.

        Steps:
        1. Check if the 'Life at Insider' section is visible on the page.
        2. Assert that the status is True.

        Parameters:
        - None

        Returns:
        - None
        """
        self.careersPage = CareersPage(self.driver)

        status = self.careersPage.is_life_at_insider()

        assert status
