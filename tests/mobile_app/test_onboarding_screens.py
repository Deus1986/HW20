import time

import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from config import config


def test_onboarding_screens():
    if config.browser_platform == "ios":
        pytest.skip("This test for android")

    with step('Verify first onboarding page opened'):
        browser.element((AppiumBy.ID, 'org.wikipedia:id/primaryTextView')).should(
            have.text('The Free Encyclopedia'))

    with step('Click continue'):
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_forward_button')).click()

    with step('Verify second onboarding page opened'):
        browser.element((AppiumBy.ID, 'org.wikipedia:id/primaryTextView')).should(have.text('New ways to explore'))

    with step('Click continue'):
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_forward_button')).click()

    with step('Verify third onboarding page opened'):
        browser.element((AppiumBy.ID, 'org.wikipedia:id/secondaryTextView')).should(
            have.text('You can make reading lists from articles'))

    with step('Click continue'):
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_forward_button')).click()

    with step('Verify fourth onboarding page opened'):
        browser.element((AppiumBy.ID, 'org.wikipedia:id/primaryTextView')).should(
            have.text('Send anonymous data'))

    with step('Click get started'):
        browser.element((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_done_button')).click()

    with step('Verify fourth onboarding page opened'):
        browser.element((AppiumBy.ID, 'org.wikipedia:id/navigation_bar_item_large_label_view')).should(
            have.text('Explore'))
