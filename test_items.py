import time
class TestLang():
    def test_language_on_page_and_check_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."
        browser.get(link)
        add_to_basket = browser.find_element_by_xpath("//input[@id = 'id_quantity']/following-sibling::button[contains(@class,btn-add-to-basket)]")
        time.sleep(30)
        assert  add_to_basket.is_displayed()
