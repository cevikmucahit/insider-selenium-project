from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    """
    Base class for Selenium WebDriver interactions.

    This class provides a set of common methods to interact with a web page using Selenium WebDriver.
    It initializes with a WebDriver instance, WebDriverWait, and ActionChains for handling interactions.
    """
    COOKIES_ACCEPT_BUTTON = (By.ID, "wt-cli-accept-all-btn")

    def __init__(self, driver):
        """
            Initializes the Base class.

            Parameters:
            - driver: WebDriver instance
            Returns:
            - None
            """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def open_url(self, url):
        """
        Opens the specified URL in the browser.

        Parameters:
        - url (str): The URL to open.

        Returns:
        - None
        """
        self.driver.get(url)

    def click_to_element(self, locator):
        """
        Clicks on the specified web element.

        Parameters:
        - locator: Tuple containing the locator strategy and value.

        Returns:
        - None
        """
        self.wait.until(ec.visibility_of_element_located(locator)).click()

    def get_element_text(self, locator):
        """
        Gets the text of the specified web element.

        Parameters:
        - locator: Tuple containing the locator strategy and value.

        Returns:
        - str: Text of the web element.
        """
        element = self.wait.until(ec.visibility_of_element_located(locator))
        return element.text

    def get_page_url(self):
        """
        Gets the current URL of the web page.

        Parameters:
        - None

        Returns:
        - str: Current URL of the web page.
        """
        return self.driver.current_url

    def is_visible(self, locator):
        """
        Checks if the specified web element is visible.

        Parameters:
        - locator: Tuple containing the locator strategy and value.

        Returns:
        - bool: True if the element is visible, False otherwise.
        """
        element = self.wait.until(ec.visibility_of_element_located(locator))
        return bool(element)

    def check_current_page(self, url):
        """
        Checks if the current page's URL matches the specified URL.

        Parameters:
        - url (str): The URL to compare.

        Returns:
        - bool: True if the current URL matches the specified URL, False otherwise.
        """
        return self.driver.current_url == url

    def is_element_exists(self, locator):
        """
        Checks if the specified web element exists on the page.

        Parameters:
        - locator: Tuple containing the locator strategy and value.

        Returns:
        - bool: True if the element exists, False otherwise.
        """
        element = self.wait.until(ec.presence_of_element_located(locator))
        return bool(element)

    def scroll_to_element(self, locator):
        """
        Scrolls the page to bring the specified web element into view.

        Parameters:
        - locator: Tuple containing the locator strategy and value.

        Returns:
        - None
        """
        js_code = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js_code, self.driver.find_element(*locator))

    def select_text_dropdown(self, locator, location):
        """
        Selects an option from a dropdown by visible text.

        Parameters:
        - locator: Tuple containing the locator strategy and value.
        - location (str): The visible text of the option to select.

        Returns:
        - None
        """
        self.wait.until(ec.visibility_of_element_located(locator))
        dropdown = Select(self.driver.find_element(*locator))
        dropdown.select_by_visible_text(location)

    def move_to_element(self, locator):
        """
        Moves the mouse pointer to the specified web element.

        Parameters:
        - locator: Tuple containing the locator strategy and value.

        Returns:
        - None
        """
        element = self.driver.find_element(*locator)
        self.action.move_to_element(element).perform()

    def wait_to_element(self, locator):
        """
        Waits for the specified web element to be present on the page.

        Parameters:
        - locator: Tuple containing the locator strategy and value.

        Returns:
        - None
        """
        self.wait.until(ec.presence_of_element_located(locator))

    def switch_to_tab(self):
        """
        Switches to the next browser tab if there is more than one open tab.

        Parameters:
        - None

        Returns:
        - None
        """
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])

    def close_cookie_warning(self):
        """
        Attempts to close the cookie warning on the page.

        Parameters:
        - None

        Returns:
        - None
        """
        try:
            self.click_to_element(self.COOKIES_ACCEPT_BUTTON)
        except Exception as e:
            print(e)
            pass
