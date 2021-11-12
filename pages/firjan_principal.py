from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Firjan_elements:
    input = "#simplequery"
    button = "header.main_header:nth-child(2) div.logo_box div.centerbx div.aux-item div.aux-busca div.lumis-service-search.lumis-service-search-search.lum-interface-type-standard:nth-child(2) form:nth-child(1) div:nth-child(1) > input:nth-child(12)"
    result = "div.innerPage:nth-child(3) div.lumis-service-search.lumis-service-search-searchResults.lum-interface-type-standard:nth-child(2) div:nth-child(1) section.center:nth-child(13) div.column_type4.tituloResultado:nth-child(1) div.countResult > span:nth-child(3)"


class Firjan_principal(Browser):

    def access_page(self, url):
        self.driver.get(url)

    def get_element(self, locator):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_elements(self, locator):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        return self.driver.find_elements(By.CSS_SELECTOR, locator)

    def get_input(self):
        self.get_element(Firjan_elements.input).send_keys("firjan")

    def get_button(self):
        self.get_element(Firjan_elements.button).click()

    def get_el_result(self):
        element = self.get_element(Firjan_elements.result)
        return element.text
