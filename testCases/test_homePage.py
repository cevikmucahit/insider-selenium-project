from configs import init_driver
from pages.homePage import HomePage
from testCases.test_base import BaseTest


class TestHomePage(BaseTest):
    def test_01_go_to_home_page(self):
        """
        Navigates to the Home Page and checks if it is displayed.

        Test Steps:
        1. Initializes the HomePage class.
        2. Opens the Home Page.
        3. Checks if the Home Page is displayed.

        Asserts:
        - True if the Home Page is displayed; False otherwise.
        """
        self.homePage = HomePage(self.driver)
        self.homePage.open_home_page()
        self.homePage.close_cookie_warning()

        status = self.homePage.is_home_page()
        assert status

    def test_02_go_to_career(self):
        """
        Navigates to the Careers Page from the Home Page and checks if the Careers Page is displayed.

        Test Steps:
        1. Initializes the HomePage class.
        2. Clicks on the 'Company' menu to reveal its options.
        3. Clicks on the 'Careers' button within the 'Company' menu.
        4. Checks if the Careers Page is displayed.

        Asserts:
        - True if the Careers Page is displayed; False otherwise.
        """
        self.homePage = HomePage(self.driver)
        self.homePage.click_company_menu()
        self.homePage.click_career_button()

        status = self.homePage.is_career_page()
        assert status
