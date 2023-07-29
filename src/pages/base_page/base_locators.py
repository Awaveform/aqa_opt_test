"""
base_locators.py

This module contains the definition of locators used in the application
on the base page.
Locators are used to identify elements on web pages using XPath or CSS
selectors.

Use locators as an input data for LocatorFactory class, example:
locator_factory = LocatorFactory(page, CareersLocators)
locator_factory.CAREERS_OFFICES_DROPDOWN.click()
locator_factory.CAREERS_OFFICES_UKR_VAL.format(office_val="UKR").click()
"""
from dataclasses import dataclass


@dataclass
class BasePageLocators:
    pass
