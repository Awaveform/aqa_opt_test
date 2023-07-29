"""
This module provides a utility class LocatorFactory designed to simplify the
usage of locators in the Playwright framework. The main goal of this class is
to make the process of locating elements on a web page more straightforward
and less error-prone.

The LocatorFactory class takes a Playwright Page object and a data class
containing the locators as arguments during initialization. It allows you to
access locators conveniently using dot notation.

If a locator requires dynamic values, you can use the format() method with
appropriate arguments to apply the required formatting.

Usage Example:
locator_factory = LocatorFactory(page, CareersLocators)
locator_factory.CAREERS_OFFICES_DROPDOWN.click()
locator_factory.CAREERS_OFFICES_UKR_VAL.format(office_val="UKR").click()
"""
from typing import Any

from playwright.async_api import Page


class LocatorFactory:
    def __init__(self, page: Page, locators: Any):
        self.page = page
        self.locators = locators

    def __getattr__(self, item: str, **kwargs) -> Any:
        locator = getattr(self.locators, item, None)
        if "{" in locator:
            return self.page.locator(selector=locator.format(**kwargs))
        if locator:
            return self.page.locator(selector=locator)
        raise AttributeError(
            f"'LocatorFactory' object has no attribute '{item}'")
