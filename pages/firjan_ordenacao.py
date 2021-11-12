from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from nose.tools import assert_equal
from pages import firjan_principal

firjan_principal = firjan_principal.Firjan_principal


class Ordenacao_elements:
    menu = "div.innerPage:nth-child(3) div.lumis-service-search.lumis-service-search-searchResults.lum-interface-type-standard:nth-child(2) section.center:nth-child(13) div.column_type2.searchOrder:nth-child(2) div.exibe-filtro:nth-child(2) div.select.selectStylized:nth-child(3) > span.close:nth-child(1)"
    orderaz = "div.innerPage:nth-child(3) div.lumis-service-search.lumis-service-search-searchResults.lum-interface-type-standard:nth-child(2) section.center:nth-child(13) div.column_type2.searchOrder:nth-child(2) div.exibe-filtro:nth-child(2) div.select.selectStylized:nth-child(3) ul:nth-child(2) > li:nth-child(3)"
    orderza = "div.innerPage:nth-child(3) div.lumis-service-search.lumis-service-search-searchResults.lum-interface-type-standard:nth-child(2) section.center:nth-child(13) div.column_type2.searchOrder:nth-child(2) div.exibe-filtro:nth-child(2) div.select.selectStylized:nth-child(3) ul:nth-child(2) > li:nth-child(4)"
    recent = "div.innerPage:nth-child(3) div.lumis-service-search.lumis-service-search-searchResults.lum-interface-type-standard:nth-child(2) section.center:nth-child(13) div.column_type2.searchOrder:nth-child(2) div.exibe-filtro:nth-child(2) div.select.selectStylized:nth-child(3) ul:nth-child(2) > li:nth-child(5)"
    old = "div.innerPage:nth-child(3) div.lumis-service-search.lumis-service-search-searchResults.lum-interface-type-standard:nth-child(2) section.center:nth-child(13) div.column_type2.searchOrder:nth-child(2) div.exibe-filtro:nth-child(2) div.select.selectStylized:nth-child(3) ul:nth-child(2) > li:nth-child(6)"
    carregar_mais = "div.innerPage:nth-child(3) div.lumis-service-search.lumis-service-search-searchResults.lum-interface-type-standard:nth-child(2) form:nth-child(1) div:nth-child(1) section.center:nth-child(13) div.column_type4.resultList:nth-child(5) > div.carregaMais:nth-child(230)"

    results = "div.resultCell h2"
    date = "div.resultCell"


class Firjan_ordenacao(Browser):
    def menu(self):
        firjan_principal.get_element(self, Ordenacao_elements.menu).click()

    def get_btn_mostrarmais(self):
        while ec.element_to_be_clickable((By.CSS_SELECTOR, Ordenacao_elements.carregar_mais)) == True:
            try:
                firjan_principal.get_element(self, Ordenacao_elements.carregar_mais).click()
            except:
                break

    def order_alphabetic_az(self):
        firjan_principal.get_element(self, Ordenacao_elements.orderaz).click()
        self.get_btn_mostrarmais()

    def order_alphabetic_za(self):
        firjan_principal.get_element(self, Ordenacao_elements.orderza).click()
        self.get_btn_mostrarmais()

    def order_recent(self):
        firjan_principal.get_element(self, Ordenacao_elements.recent).click()
        self.get_btn_mostrarmais()

    def order_old(self):
        firjan_principal.get_element(self, Ordenacao_elements.old).click()
        self.get_btn_mostrarmais()

    def get_results(self):
        results = []
        all_results = firjan_principal.get_elements(self, Ordenacao_elements.results)

        for result_el in all_results:
            results.append(result_el.text)

        return results

    def get_dates(self):
        dates = []
        elements = firjan_principal.get_elements(self, Ordenacao_elements.date)

        for element in elements:
            dates.append(element.get_attribute("data-publicacao"))

        dates_filter = filter(None.__ne__, dates)
        dates = list(dates_filter)

        return dates

    def test_order_az(self):
        results = self.get_results()

        elements_orded = results
        sorted(elements_orded)
        return (assert_equal(results, elements_orded))

    def test_order_za(self):
        results = self.get_results()

        elements_reversed = results
        reversed(elements_reversed)
        return (assert_equal(results, elements_reversed))

    def test_order_recent(self):
        dates = self.get_dates()

        dates_orded = dates
        sorted(dates_orded)
        return (assert_equal(dates, dates_orded))

    def test_order_old(self):
        dates = self.get_dates()

        dates_reversed = dates
        reversed(dates_reversed)
        return (assert_equal(dates, dates_reversed))
