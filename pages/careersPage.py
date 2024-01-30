import time

from selenium.webdriver.common.by import By

from pages.base import Base


class CareersPage(Base):
    CAREERS_URL = "https://useinsider.com/careers/"
    DEPARTMENTS = (By.CSS_SELECTOR, ".job-item h3")
    NEXT_LOCATION_BUTTON = (By.CSS_SELECTOR, "#career-our-location .location-slider-next")
    LIFE_AT_INSIDER = (By.CSS_SELECTOR, "[data-id='a8e7b90']")
    OUR_LOCATIONS = (By.ID, "career-our-location")
    OUR_LOCATIONS_NAMES = (By.CSS_SELECTOR, ".location-info p")
    SEE_ALL_TEAMS_BUTTON = (By.CLASS_NAME, "loadmore")

    def __init__(self, driver):
        """
        Initializes the CareersPage class.

        Parameters:
        - driver: The Selenium WebDriver instance used for browser automation.
        """
        super().__init__(driver)

    def scroll_to_our_location(self):
        """Scrolls the page to bring the 'Our Locations' section into view."""
        self.scroll_to_element(self.OUR_LOCATIONS)

    def scroll_to_departments(self):
        """Scrolls the page to bring the department names into view."""
        self.scroll_to_element(self.DEPARTMENTS)

    def open_careers_page(self):
        """Opens the Careers Page by navigating to the specified CAREERS_URL."""
        self.open_url(self.CAREERS_URL)

    def click_next_location_button(self):
        """Clicks on the button to navigate to the next location in the 'Our Locations' section."""
        self.click_to_element(self.NEXT_LOCATION_BUTTON)

    def add_locations_to_list(self, actual_list):
        """
        Adds the names of locations from the 'Our Locations' section to the provided list.

        Parameters:
        - actual_list: The list to which location names will be added.
        """
        our_location = self.driver.find_elements(*self.OUR_LOCATIONS_NAMES)
        for i in our_location:
            actual_list.append(i.text)
            self.click_to_element(self.NEXT_LOCATION_BUTTON)
            time.sleep(0.4)

    def add_departments_to_list(self, actual_list):
        """
        Adds the names of departments on the Careers Page to the provided list.

        Parameters:
        - actual_list: The list to which department names will be added.
        """
        department = self.driver.find_elements(*self.DEPARTMENTS)
        for i in department:
            actual_list.append(i.text)

    def click_see_all_teams_button(self):
        """Clicks on the 'See All Teams' button."""
        self.click_to_element(self.SEE_ALL_TEAMS_BUTTON)

    def is_life_at_insider(self):
        """
        Checks if the 'Life at Insider' section is present on the Careers Page.

        Returns:
        - True if the 'Life at Insider' section is present; False otherwise.
        """
        return self.is_element_exists(self.LIFE_AT_INSIDER)
