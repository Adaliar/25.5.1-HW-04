from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 120)

    def __get_selenium_by(self, find_by):
        locating = {
            'id': By.ID,
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH
        }
        return locating[find_by]

    def get_log_locator(self, locator):
        loc_data = {
            'AUTH_LOG': 'username',
            'AUTH_PASSWORD': 'password',
            'AUTORIZATION': 'kc-login',
            'CHECK': 'lk-btn',
            'REGISTRATION': 'kc-register',
            'NAME': '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input',
            'LASTNAME': '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input',
            'ADDRESS': 'address',
            'PASS_CONF': 'password-confirm',
            'REG_BTN': '//*[@id="page-right"]/div/div/div/form/button',
            'LINK': '//*[@id="page-right"]/div/div/div/form/div[4]/a',
            'RECOVERY': 'forgot_password',
            'CONT_BTN': 'reset',
            'CHOOSE': '//*[@id="page-right"]/div/div/div/form/div/label[1]/span/span[1]',
            'CHOOSE_2': '//*[@id="page-right"]/div/div/div/form/div/label[2]/span/span[3]/span[1]',
            'NEW_PASS': 'password-new',
            'SAVE_BTN': 't-btn-reset-pass',
            'CONT_2': '//*[@id="page-right"]/div/div/div/form/button[1]',
            'ODN_BTN': 'oidc_ok',
            'LOG_ODN': 'field_email',
            'PASS_ODN': 'field_password',
            'ENTER_ODN': '//*[@id="widget-el"]/div[2]/div/div/div[4]/input',
            'MAIL_BTN': 'oidc_mail',
            'ENTER_MAIL': '//*[@id="login-form"]/div[2]/button',
            'LOG_MAIL': 'login',
            'YA_BTN': 'oidc_ya',
            'LOG_YA': 'passp-field-login',
            'ENTER_YA': '//*[@id="passp:sign-in"]',
            'YA_PASS': '//*[@id="passp-field-passwd"]',
            'SELECT': 't-btn-tab-ls'

        }
        return loc_data[locator]

    def get_user_info(self, find_by, locator):
        return self.__wait.until(
            ec.visibility_of_element_located((self.__get_selenium_by(find_by), self.get_log_locator(locator))))

    def check_text(self, find_by, locator):
        return self.__wait.until(
            ec.visibility_of_element_located((self.__get_selenium_by(find_by), self.get_log_locator(locator))))
