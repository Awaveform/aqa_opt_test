"""
careers_locators.py

This module contains the definition of locators used in the application
on the 'Careers' page.
Locators are used to identify elements on web pages using XPath or CSS
selectors.

Use locators as an input data for LocatorFactory class, example:
locator_factory = LocatorFactory(page, CareersLocators)
locator_factory.CAREERS_OFFICES_DROPDOWN.click()
locator_factory.CAREERS_OFFICES_UKR_VAL.format(office_val="UKR").click()
"""
from dataclasses import dataclass

from src.pages.base_page.base_locators import BasePageLocators


@dataclass
class CareersLocators(BasePageLocators):

    CAREERS_AQA_JOB_TITLE = "//div[@class='job-card__title']" \
                            "//a[text()='QA Automation Engineer']"
    CAREERS_BRAND_LINK = "//a[@class='brand']"
    CAREERS_OFFICES_DROPDOWN = "//div[contains(@class, 'job-locations')]" \
                               "//span[contains(text(), 'All')]"
    CAREERS_OFFICES_UKR_VAL = "//li[contains(text(), '{office_val}')]"
