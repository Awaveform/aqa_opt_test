"""
This module provides a utility class LocatorFactory designed to simplify the
usage of locators in the Playwright framework. The main goal of this class is
to make the process of locating elements on a web page more straightforward
and less error-prone.
"""
from typing import Union

from playwright.async_api import Page, Locator

from src.pages.base_page.base_locators import BasePageLocators
from src.pages.careers_page.careers_locators import CareersLocators


class LocatorFactory:
    """
    The LocatorFactory class takes a Playwright Page object and a data class
    containing the locators as arguments during initialization. It allows you
    to access locators conveniently using dot notation.

    If a locator requires dynamic values, you can use the format() method with
    appropriate arguments to apply the required formatting.

    Usage Example:
    locator_factory = LocatorFactory(page, CareersLocators)
    locator_factory.CAREERS_OFFICES_DROPDOWN.click()
    locator_factory.CAREERS_OFFICES_UKR_VAL.format(office_val="UKR").click()
    """
    def __init__(
            self, page: Page,
            locators: Union[BasePageLocators, CareersLocators]
    ):
        self.page = page
        self.locators = locators

    def __getattr__(self, item: str, **kwargs) -> Locator:
        """
        Changes getting of locator obj to these:
        self.locators: This refers to an object (in this case, self.locators)
        from which you want to retrieve the attribute value.
        None: This is the default value that getattr returns if the attribute
        specified by item does not exist in the object self.locators.
        If the attribute exists, getattr will return its value.
        Raises 'AttributeError' if invalid value provided.

        :param item: It is a string that represents the name of the attribute
        you want to access within the object self.locators.
        :param kwargs: Params for formatting of the locator's string value.
        :return: Playwright's locator object which can be used
        for interactions.
        """
        locator = getattr(self.locators, item, None)
        if "{" in locator:
            return self.page.locator(selector=locator.format(**kwargs))
        if locator:
            return self.page.locator(selector=locator)
        raise AttributeError(
            f"'LocatorFactory' object has no attribute '{item}'")
