#!/usr/bin/env python

from pypom import Page, Region
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UnitedUs(Page):

    _page_loaded_locator = (By.CSS_SELECTOR, '.list-container h2 span')
    _filter_results_locator = (By.CSS_SELECTOR, '.list-listener-container article')
    _results_drawer = (By.CSS_SELECTOR, '.open')

    def wait_for_page_to_load(self):
        self.wait.until(lambda s: self.find_element(*self._page_loaded_locator).text != '')
        return self

    @property
    def is_results_drawer_open(self):
        return self.find_element(*self._results_drawer).is_displayed()

    @property
    def filters(self):
        return self.Filters(self)

    @property
    def results(self):
        self.wait_for_page_to_load()
        return [self.Result(self, el) for el in self.find_elements(*self._filter_results_locator)]

    @property
    def detailed_results(self):
        return self.ResultDetailsDrawer(self, self.find_element(*self._results_drawer))

    class Filters(Region):

        _name_locator = (By.ID, 'searchInput')
        _location_locator = (By.ID, 'filterInputLocationSearch')

        def search_by_name(self, search_text):
            name_search = self.find_element(*self._name_locator)
            name_search.send_keys(search_text)
            name_search.send_keys(Keys.RETURN)

        def search_by_location(self, location_text):
            name_search = self.find_element(*self._location_locator)
            name_search.send_keys(location_text)
            name_search.send_keys(Keys.RETURN)

        # service type
        def set_employment_type(employment_options):
            for selection in employment_options:


    class Result(Region):

        _name_locator = (By.CLASS_NAME, 'name')
        _provided_by_locator = (By.CSS_SELECTOR, '.dark span')
        _address_locator = (By.CLASS_NAME, 'address')
        _services_locator = (By.CLASS_NAME, 'service')

        @property
        def name(self):
            return self.find_element(*self._name_locator).text

        @property
        def provider_name(self):
            return self.find_element(*self._provided_by_locator).text

        @property
        def address(self):
            return self.find_element(*self._address_locator).text

        @property
        def services(self):
            return self.find_element(*self._services_locator).text

        def click_result(self):
            self.find_element(*self._name_locator).click()
            return self

    class ResultDetailsDrawer(Region):

        _name_locator = (By.CLASS_NAME, 'name')
        _provided_by_locator = (By.CSS_SELECTOR, '.dark span')
        _address_locator = (By.CLASS_NAME, 'address')
        _services_locator = (By.CLASS_NAME, 'service')

        @property
        def name(self):
            return self.find_element(*self._name_locator).text

        @property
        def provider_name(self):
            return self.find_element(*self._provided_by_locator).text

        @property
        def address(self):
            return self.find_element(*self._address_locator).text

        @property
        def services(self):
            return self.find_element(*self._services_locator).text
