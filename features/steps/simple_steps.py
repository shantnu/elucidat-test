from behave import given, then
from playwright.sync_api import sync_playwright

@given('I open the Elucidat webpage')
def step_given_i_open_the_webpage(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False, slow_mo=500)
    context.page = context.browser.new_page()
    context.page.goto("https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a")

@then('the header should be "{expected_header}"')
def step_then_the_header_should_be(context, expected_header):
    header = context.page.get_by_role("heading", name=expected_header).text_content()
    assert header == expected_header, f"Expected header to be '{expected_header}', but got '{header}'"
    context.browser.close()
    context.playwright.stop()
