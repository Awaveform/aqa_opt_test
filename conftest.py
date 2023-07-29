import os
from typing import Any

import pytest
import sys

import pytest_asyncio
from loguru import logger
from playwright.async_api import async_playwright

from src.pages.base_page.base_page import BasePage
from src.pages.careers_page.careers_locators import CareersLocators
from src.pages.careers_page.careers_page import CareersPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chromium",
        help="Specify the browser type: chromium, firefox, or webkit"
    )


@pytest.fixture(scope="session", autouse=True)
def setup_loguru_logging():
    # Set up Loguru logger with custom format for console and file handlers
    log_level_file = os.getenv("LOG_FILE_LEVEL")
    log_format_file = os.getenv("LOG_FILE_FORMAT")
    log_cli_format = os.getenv("LOG_CLI_FORMAT")

    # Set up Loguru logger with custom format for console and file handlers
    logger.remove()
    logger.add(
        sink="last_test_run.log",
        level=log_level_file,
        format=log_format_file,
        mode="w"
    )
    logger.add(
        sink=sys.stdout,
        level=log_level_file,
        format=log_cli_format
    )


@pytest_asyncio.fixture(name="browser_type_launch_args")
@pytest.mark.asyncio
async def _browser_type_launch_args():
    return {
        "headless": False,  # Override the default headless mode
        "slow_mo": 0,    # Additional custom launch argument, e.g., slow_mo
        "devtools": False,  # Open devtools
        "args": ["--start-maximized"],
    }


@pytest_asyncio.fixture(name="browser_context_args")
@pytest.mark.asyncio
async def _browser_context_args():
    return {
        "no_viewport": True,  # Override the default headless mode
    }


@pytest_asyncio.fixture(name="start_async_browser")
@pytest.mark.asyncio
async def _start_async_browser(
        browser_type_launch_args,
        browser_context_args,
        request
) -> Any:
    selected_browser = request.config.getoption("--browser_name")
    async with async_playwright() as apw:

        launch_function = {
            "chromium": apw.chromium.launch,
            "firefox": apw.firefox.launch,
            "webkit": apw.webkit.launch
        }.get(selected_browser, apw.chromium.launch)
        browser = await launch_function(**browser_type_launch_args)

        context = await browser.new_context(**browser_context_args)
        page = await context.new_page()

        yield page

        await browser.close()


@pytest.fixture(name="optimove_page")
def base_page(start_async_browser):
    # Create an instance of OptimovePage with the page object
    return BasePage(page=start_async_browser)


@pytest.fixture(name="optimove_page")
def careers_page(start_async_browser):
    # Create an instance of OptimovePage with the page object
    return CareersPage(page=start_async_browser)
