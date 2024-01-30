import time
from configs import init_driver
from pages.qualityAssurancePage import QualityAssurancePage
from testCases.test_base import BaseTest


class TestQualityAssurancePage(BaseTest):

    def test_01_select_location(self):
        """
        Test method to check if selecting 'Istanbul, Turkey' from the location dropdown works correctly.

        Steps:
        1. Open the Quality Assurance Page.
        2. Close the cookie warning.
        3. Click on the 'See All QA Jobs' button.
        4. Select 'Istanbul, Turkey' from the location dropdown.
        5. Assert that the selected location matches the expected location.

        Parameters:
        - None

        Returns:
        - None
        """
        self.qualityAssurancePage = QualityAssurancePage(self.driver)
        self.qualityAssurancePage.open_quality_assurance_page()
        self.qualityAssurancePage.close_cookie_warning()
        self.qualityAssurancePage.click_see_all_qa_jobs_button()
        self.qualityAssurancePage.select_location_istanbul_turkey()

        assert "Istanbul, Turkey" == self.qualityAssurancePage.get_location_dropdown_text()

    def test_02_select_department(self):
        """
        Test method to check if selecting 'Quality Assurance' from the department dropdown works correctly.

        Steps:
        1. Select 'Quality Assurance' from the department dropdown.
        2. Assert that the selected department matches the expected department.

        Parameters:
        - None

        Returns:
        - None
        """
        self.qualityAssurancePage = QualityAssurancePage(self.driver)
        self.qualityAssurancePage.select_department()

        assert "Quality Assurance" == self.qualityAssurancePage.gef_department_dropdown_text()

    def test_03_check_job_list(self):
        """
        Test method to check if the job list is present on the Quality Assurance Page.

        Steps:
        1. Check if the job list is present on the page.
        2. Assert that the status is True.

        Parameters:
        - None

        Returns:
        - None
        """
        self.qualityAssurancePage = QualityAssurancePage(self.driver)

        status = self.qualityAssurancePage.is_job_list()

        assert status

    def test_04_job_list_count(self):
        """
        Test method to check if the count of positions in the Quality Assurance department
        matches the total number of positions listed.

        Steps:
        1. Check the count of positions for 'Istanbul, Turkey' in the 'Quality Assurance' department.
        2. Check the total number of positions listed on the page.
        3. Assert that the count of positions matches the total number of positions.

        Parameters:
        - None

        Returns:
        - None
        """
        time.sleep(1)
        self.qualityAssurancePage = QualityAssurancePage(self.driver)

        qa_department_count = self.qualityAssurancePage.check_department_contains()

        assert qa_department_count == self.qualityAssurancePage.get_department_len()

    def test_05_go_to_position_role(self):
        """
        Test method to check if navigating to each position's detailed role page works correctly.

        Steps:
        1. Wait for the position list to be present.
        2. Scroll to the position header.
        3. Check if the information for each position matches between the current page and the Lever application page.
        4. Assert that the status is True.

        Parameters:
        - None

        Returns:
        - None
        """
        self.qualityAssurancePage = QualityAssurancePage(self.driver)
        self.qualityAssurancePage.wait_to_position_list()
        self.qualityAssurancePage.scroll_to_element_position()
        time.sleep(1)

        status = self.qualityAssurancePage.check_each_position_info()

        assert status
