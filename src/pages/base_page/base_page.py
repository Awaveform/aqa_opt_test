"""

"""
from dataclasses import dataclass
from typing import Type, Any

from loguru import logger
from playwright.async_api import Page

from src.pages.base_page.base_locators import BasePageLocators
from src.utilities.locators_factory import LocatorFactory


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
    def __init__(self, page: Page, locators: Any):
        self.page = page
        self.logger = logger
        self.loc = LocatorFactory(
            page=page,
            locators=locators
        )
