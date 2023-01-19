# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestAddtextaccesorii():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_addtextaccesorii(self):
    # Test name: addtext_accesorii
    # Step # | name | target | value
    # 1 | open | http://34.118.122.203/administration/index.php?controller=AdminLogin&logout=1&token=9a6620764c248cdd5422f2a6b5e18bb4 |
    self.driver.get(
      "http://34.118.122.203/administration/index.php?controller=AdminLogin&logout=1&token=9a6620764c248cdd5422f2a6b5e18bb4")
    # 2 | setWindowSize | 1382x744 |
    self.driver.set_window_size(1382, 744)
    # 3 | type | id=email | leahivanovici@gmail.com
    self.driver.find_element(By.ID, "email").send_keys("leahivanovici@gmail.com")
    # 4 | type | id=passwd | 123456789
    self.driver.find_element(By.ID, "passwd").send_keys("123456789")
    # 5 | click | id=submit_login |
    self.driver.find_element(By.ID, "submit_login").click()
    time.sleep(2)
    # 6 | click | css=#subtab-AdminCatalog span |
    self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog span").click()
    time.sleep(5)
    # 7 | click | linkText=Categories |
    self.driver.find_element(By.LINK_TEXT, "Categories").click()
    # 8 | mouseOver | css=#tr_2_6_1 .btn-group > .tooltip-link |
    element = self.driver.find_element(By.CSS_SELECTOR, "#tr_2_6_1 .btn-group > .tooltip-link")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 9 | mouseOut | css=#tr_2_6_1 .btn-group > .tooltip-link |
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element_with_offset(element, 0, 0).perform()
    # 10 | click | css=#tr_2_6_1 .btn-link |
    self.driver.find_element(By.CSS_SELECTOR, "#tr_2_6_1 .btn-link").click()
    # 11 | click | css=.show > .grid-edit-row-link |
    self.driver.find_element(By.CSS_SELECTOR, ".show > .grid-edit-row-link").click()
    # 12 | runScript | window.scrollTo(0,27) |
    self.driver.execute_script("window.scrollTo(0,27)")
    time.sleep(5)
    # 13 | selectFrame | index=0 |
    self.driver.switch_to.frame(0)
    # 14 | click | css=p |
    self.driver.find_element(By.CSS_SELECTOR, "p").click()
    # 15 | editContent | id=tinymce | <p>Items and accessories for your desk, kitchen or living room. Make your house a home with our eye-catching designs. Improspateaza-ti casa cu cele mai recente accesorii PrestaShop.</p>
    element = self.driver.find_element(By.ID, "tinymce")
    self.driver.execute_script(
      "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Items and accessories for your desk, kitchen or living room. Make your house a home with our eye-catching designs. Improspateaza-ti casa cu cele mai recente accesorii PrestaShop.</p>'}",
      element)
    # 16 | selectFrame | relative=parent |
    self.driver.switch_to.default_content()
    # 17 | click | id=save-button |
    self.driver.find_element(By.ID, "save-button").click()
    assert "Successful update." in self.driver.page_source
    # 18 | open | /en/ |
    self.driver.get("http://34.118.122.203/en/")
    # 19 | setWindowSize | 1050x708 |
    self.driver.set_window_size(1050, 708)
    # 20 | click | css=#category-6 > .dropdown-item |
    self.driver.find_element(By.CSS_SELECTOR, "#category-6 > .dropdown-item").click()
    assert "Improspateaza-ti casa cu cele mai recente accesorii PrestaShop." in self.driver.find_element(By.CLASS_NAME, "text-muted").text
