import time

from selenium.webdriver.common.by import By

from pages.base import Base
from selenium.webdriver.support.ui import Select


class QualityAssurancePage(Base):
    QUALITY_ASSURANCE_URL = "https://useinsider.com/careers/quality-assurance/"
    SEE_ALL_QA_JOBS_BUTTON = (By.CSS_SELECTOR, ".button-group.flex-row a")
    LOCATION_DROPDOWN = (By.ID, "filter-by-location")
    DEPARTMENT_DROPDOWN = (By.ID, "filter-by-department")
    POSITION_LIST_ITEM = (By.CLASS_NAME, "position-list-item")
    POSITION_TITLE = (By.CLASS_NAME, "position-title")
    VIEW_ROLE_BUTTON = (By.CSS_SELECTOR, ".position-list-item a")
    JOB_LIST = (By.ID, "jobs-list")
    POSITION_HEADER = (By.CSS_SELECTOR, "#career-position-list h3")
    LEVER_POSITION_TITLE = (By.CSS_SELECTOR, ".posting-headline h2")

    def open_quality_assurance_page(self):
        """
        Opens the Quality Assurance Jobs Page by navigating to the specified QUALITY_ASSURANCE_URL.

        Parameters:
        - None

        Returns:
        - None
        """
        self.open_url(self.QUALITY_ASSURANCE_URL)

    def click_see_all_qa_jobs_button(self):
        """
        Clicks on the 'See All QA Jobs' button.

        Parameters:
        - None

        Returns:
        - None
        """
        self.click_to_element(self.SEE_ALL_QA_JOBS_BUTTON)

    def select_location_istanbul_turkey(self):
        """
        Selects the location 'Istanbul, Turkey' from the location dropdown.

        Parameters:
        - None

        Returns:
        - None
        """
        self.select_text_dropdown(locator=self.LOCATION_DROPDOWN, location="Istanbul, Turkey")

    def select_department(self):
        """
        Selects the 'Quality Assurance' department from the department dropdown.

        Parameters:
        - None

        Returns:
        - None
        """
        self.select_text_dropdown(locator=self.DEPARTMENT_DROPDOWN, location="Quality Assurance")

    def get_location_dropdown_text(self):
        """
        Retrieves the text of the selected option in the location dropdown.

        Parameters:
        - None

        Returns:
        - Text of the selected location option.
        """
        element = Select(self.driver.find_element(*self.LOCATION_DROPDOWN))
        return element.first_selected_option.text

    def gef_department_dropdown_text(self):
        """
        Retrieves the text of the selected option in the department dropdown.

        Parameters:
        - None

        Returns:
        - Text of the selected department option.
        """
        element = Select(self.driver.find_element(*self.DEPARTMENT_DROPDOWN))
        return element.first_selected_option.text

    def is_job_list(self):
        """
        Checks if the job list is present on the page.

        Parameters:
        - None

        Returns:
        - True if the job list is present; False otherwise.
        """
        return self.is_element_exists(self.JOB_LIST)

    def check_department_contains(self):
        """
        Checks the number of positions listed for 'Istanbul, Turkey' in the 'Quality Assurance' department.

        Parameters:
        - None

        Returns:
        - The count of positions for 'Istanbul, Turkey' in the 'Quality Assurance' department.
        """
        position_list = self.driver.find_elements(*self.POSITION_LIST_ITEM)
        actual_count = 0
        for i in position_list:
            if i.get_attribute("data-location") == "istanbul-turkey" and "qualityassurance" == i.get_attribute(
                    "data-team"):
                actual_count += 1
        return actual_count

    def get_department_len(self):
        """
        Retrieves the total number of positions listed on the page.

        Parameters:
        - None

        Returns:
        - The total number of positions listed on the page.
        """
        elements = self.driver.find_elements(*self.POSITION_LIST_ITEM)
        return len(elements)

    def scroll_to_element_position(self):
        """
        Scrolls to the position header.

        Parameters:
        - None

        Returns:
        - None
        """
        self.scroll_to_element(self.POSITION_HEADER)

    def focus_to_position(self):
        """
        Moves the mouse cursor to a position in the position list.

        Parameters:
        - None

        Returns:
        - None
        """
        self.move_to_element(self.POSITION_LIST_ITEM)

    def click_view_role_button(self):
        """
        Clicks on the 'View Role' button.

        Parameters:
        - None

        Returns:
        - None
        """
        self.click_to_element(self.VIEW_ROLE_BUTTON)

    def wait_to_view_role_button(self):
        """
        Waits for the 'View Role' button to be present.

        Parameters:
        - None

        Returns:
        - None
        """
        self.wait_to_element(self.VIEW_ROLE_BUTTON)

    def wait_to_position_list(self):
        """
        Waits for the position list to be present.

        Parameters:
        - None

        Returns:
        - None
        """
        self.wait_to_element(self.POSITION_LIST_ITEM)

    def switch_to_lever_application_page(self):
        """
        Switches to the Lever application page by opening it in a new tab.

        Parameters:
        - None

        Returns:
        - None
        """
        self.switch_to_tab()

    def check_each_position_info(self):
        """
        Checks if the information for each position matches between the current page and the Lever application page.

        Parameters:
        - None

        Returns:
        - True if the information matches for each position; False otherwise.
        """
        base = self.driver.current_window_handle
        positions = self.driver.find_elements(*self.POSITION_LIST_ITEM)

        for position in positions:
            current_position_title = position.find_element(*self.POSITION_TITLE).text
            self.action.move_to_element(position).perform()

            position.find_element(*self.VIEW_ROLE_BUTTON).click()
            self.switch_to_lever_application_page()

            lever_position_title = self.driver.find_element(*self.LEVER_POSITION_TITLE).text

            self.driver.close()
            self.driver.switch_to.window(base)
            time.sleep(1)

            if current_position_title != lever_position_title:
                return False

        return True
