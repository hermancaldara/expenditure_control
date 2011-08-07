import unittest
import time

from splinter.browser import Browser

from should_dsl import should


class TestAcceptance(unittest.TestCase):

    def setUp(self):
        self.browser = Browser()

    def test_add_an_expense(self):
        self.browser.visit('http://localhost:8000/')
        self.browser.fill('value', '20.0')
        self.browser.fill('category', 'food')
        self.browser.fill('description', 'Rice')
        self.browser.fill('date', '01/01/2011')
        self.browser.find_by_id('submit').first.click()
        self.browser.is_text_present('Expense saved with success!') |should| be(True)

    def tearDown(self,):
        self.browser.quit()
