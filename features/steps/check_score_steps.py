from behave import given, then, step
from playwright.sync_api import sync_playwright
import re


@step('Go to the score page')
def step_then_the_header_should_be(context):
    # Buttons contains images that confuses playwright??? so doing this, search for start
    button_span = context.page.locator('span.button__text:has-text("START")')
    button_span.click()

    # Wait until the text appears on the page

    context.page.wait_for_selector('strong:has-text("FINDING THE TRUTH")')



@then('the score should only be a number')
def step_then_score(context):
    # force a page reload as has old data
    context.page.reload()
    context.page.wait_for_selector('strong:has-text("FINDING THE TRUTH")')

    elements = context.page.query_selector_all('.htmlText')

    text_content = elements[1].text_content()

    print(text_content)
    pattern = r'Your score so far:(.*)'
    score_found = re.search(pattern, text_content)[1]

    assert(score_found.isdigit()) # assert if any non-digits found
    context.browser.close()
    context.playwright.stop()
