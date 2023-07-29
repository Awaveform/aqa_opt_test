"""
base_locators.py

This module contains the definition of locators used in the application.
Locators are used to identify elements on web pages using XPath or CSS
selectors.

Locators are defined as class attributes in the BaseLocators class.

If value is str, example of usage:
    await self.page.locator(self.loc.OFFICES_UKR_VAL.format(office_val))
If value is locator object, example of usage:
    await self.loc.OFFICES_DROPDOWN.click()
"""
from dataclasses import dataclass


@dataclass
class BasePageLocators:
    pass
