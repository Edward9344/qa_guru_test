import pytest
from selene import browser, have

@pytest.fixture
def screen_resolution():
    browser.config.window_height = '1080'
    browser.config.window_width = '1920'
    browser.quit()
def test_search_google(screen_resolution):
    browser.open('https://www.google.com/')
    browser.element('[class="gLFyf"]').click().type("saaaaaaaaaaaaaaaaaaaaaaaaaaaadddddddddddddddddddddd").press_enter()
    browser.element('[class="v3jTId"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))