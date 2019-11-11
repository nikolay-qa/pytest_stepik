from selenium.common.exceptions import NoSuchElementException
# import time       # just uncomment it to test this script


def test_guest_should_see_add_to_basket_button(browser, lang):
    link = f"http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(10)
    # time.sleep(10) # and this one too:)
    xpath_for_test = "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"
    try:
        browser.find_element_by_xpath(xpath_for_test)
        print("Button is present.")
    except NoSuchElementException:
        assert False, "There is no button on this web page!"



