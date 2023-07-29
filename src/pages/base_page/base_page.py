"""

"""

from loguru import logger
from playwright.async_api import Page


class BasePage:
    """
    The BasePage class represents a base page for the website.

    This class provides common functionality and properties that are shared
    among multiple pages in the website.

    Attributes:
        page (Page): The Playwright Page object representing the current page.
        logger (Logger): The Loguru logger object for logging messages and
        events.
    """
    def __init__(self, page: Page):
        self.page = page
        self.logger = logger
