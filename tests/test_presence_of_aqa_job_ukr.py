import pytest


@pytest.mark.asyncio
# @pytest.mark.repeat(10)  # Uncomment to check stability
async def test_presence_of_aqa_job_ukr(optimove_page) -> None:
    """
    Test case: #
    Jura issues: ##
    :param optimove_page: fixture of the page model 'Careers'.
    :return: None.
    """
    await optimove_page.open_careers_page()
    await optimove_page.hover_over_brand_link()
    await optimove_page.click_offices_dropdown()
    await optimove_page.select_ukr_office()
    await optimove_page.scroll_to_aqa_job_title()
    await optimove_page.verify_visibility_of_aqa_job_title()
