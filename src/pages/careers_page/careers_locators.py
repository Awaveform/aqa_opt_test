"""
careers_locators.py

This module contains the definition of locators used in the application.
Locators are used to identify elements on web pages using XPath or CSS
selectors.

Locators are defined as class attributes in the CareersLocators class.

If value is str, example of usage:
    await self.page.locator(self.loc.OFFICES_UKR_VAL.format(office_val))
If value is locator object, example of usage:
    await self.loc.OFFICES_DROPDOWN.click()
"""
from playwright.async_api import Page


class CareersLocators:

    def __init__(self, page: Page):

        self.AQA_JOB_TITLE = page.locator("//div[@class='job-card__title']//a[text()='QA Automation Engineer']")
        self.BRAND_LINK = page.locator("//a[@class='brand']")
        self.OFFICES_DROPDOWN = page.locator("//div[contains(@class, 'job-locations')]//span[contains(text(), 'All')]")
        self.OFFICES_UKR_VAL = "//li[contains(text(), '{0}')]"
        self.AQA_JOB_TITLE = page.locator("//div[@class='job-card__title']//a[text()='QA Automation Engineer']")
