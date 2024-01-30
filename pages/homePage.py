from selenium.webdriver.common.by import By

from configs.constants import BASE_URL
from pages.base import Base


class HomePage(Base):
    CAREERS_BUTTON = (By.CSS_SELECTOR, ".new-menu-dropdown-layout-6-mid-container a:nth-child(2)")
    CAREERS_PAGE_ROUTER = (By.CSS_SELECTOR, "router.career-page")
    COMPANY_MENU = (By.CSS_SELECTOR, "#navbarNavDropdown ul li:nth-child(6)")
    HOME_PAGE_ROUTER = (By.CSS_SELECTOR, "router.home-page")

    def __init__(self, driver):
        """
        Initializes the HomePage class.

        Parameters:
        - driver: The Selenium WebDriver instance used for browser automation.
        """
        super().__init__(driver)

    def open_home_page(self):
        """
        Opens the Home Page by navigating to the specified BASE_URL.

        Returns:
        - None
        """
        self.open_url(BASE_URL)

    def is_home_page(self):
        """
        Checks if the Home Page is currently displayed by verifying the existence of the HOME_PAGE_ROUTER element.

        Returns:
        - True if the Home Page is displayed; False otherwise.
        """
        return self.is_element_exists(self.HOME_PAGE_ROUTER)

    def click_company_menu(self):
        """
        Clicks on the 'Company' menu to reveal its options.

        Returns:
        - None
        """
        self.click_to_element(self.COMPANY_MENU)

    def click_career_button(self):
        """
        Clicks on the 'Careers' button within the 'Company' menu.

        Returns:
        - None
        """
        self.click_to_element(self.CAREERS_BUTTON)

    def is_career_page(self):
        """
        Checks if the Careers Page is currently displayed by verifying the existence of the CAREERS_PAGE_ROUTER element.

        Returns:
        - True if the Careers Page is displayed; False otherwise.
        """
        return self.is_element_exists(self.CAREERS_PAGE_ROUTER)
