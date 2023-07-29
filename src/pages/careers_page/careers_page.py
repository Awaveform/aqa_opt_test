from typing import Type

from playwright.async_api import Page

from src.pages.base_page.base_page import BasePage
from src.pages.careers_page.careers_locators import CareersLocators
from src.pages.url_routs import PagesURLs


class CareersPage(BasePage):
    """
    The CareersPage class represents the careers page of the website.

    This page contains functionality and properties specific to the careers
    page.

    Attributes:
        page (Page): The Playwright Page object representing the current page.
        logger (Logger): The Loguru logger object for logging messages and
        events.
    """
    def __init__(
            self, page: Page,
            locators: Type[CareersLocators] = CareersLocators
    ):
        super().__init__(page=page, locators=locators)

    async def open_careers_page(self) -> None:
        """
        Open URL 'optimove.com/careers'.
        :return: None.
        """
        self.logger.info("Navigating to the careers page.")
        await self.page.goto(
            url=PagesURLs.BASE.value + PagesURLs.CAREERS.value
        )

    async def hover_over_brand_link(self) -> None:
        """
        Focus the brand picture in the header with 'hover' action.
        :return: None.
        """
        self.logger.info("Hovering over the brand link.")
        await self.loc.CAREERS_BRAND_LINK.hover()

    async def click_offices_dropdown(self) -> None:
        """
        Expand the dropdown 'Offices'.
        :return: None.
        """
        self.logger.info("Clicking on the offices dropdown.")
        await self.loc.CAREERS_OFFICES_DROPDOWN.scroll_into_view_if_needed()
        await self.loc.CAREERS_OFFICES_DROPDOWN.click()

    async def select_ukr_office(self, office_val: str = "UKR") -> None:
        """
        Select an option in the dropdown 'Offices'.
        :return: None.
        """
        self.logger.info(f"Selecting the {office_val} office.")
        await self.loc.CAREERS_OFFICES_DROPDOWN.click()

    async def scroll_to_aqa_job_title(self) -> None:
        """
        Scroll to the first "QA Automation Engineer" job title.
        :return: None.
        """
        self.logger.info("Scrolling to the AQA job title.")
        await self.loc.CAREERS_AQA_JOB_TITLE.first.scroll_into_view_if_needed()

    async def verify_visibility_of_aqa_job_title(self) -> None:
        """
        Wait for visibility of the "QA Automation Engineer" job title.
        Otherwise, raise TimeoutError.
        :return: None.
        """
        await self.loc.CAREERS_AQA_JOB_TITLE.first.wait_for(
            timeout=10000, state="visible"
        )
