from base import SeleniumBase


class Selecting(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_log_field(self):
        return self.get_user_info('id', 'AUTH_LOG')

    def get_password(self):
        return self.get_user_info('id', 'AUTH_PASSWORD')

    def auto_btn(self):
        return self.get_user_info('id', 'AUTORIZATION')

    def checking(self):
        return self.get_user_info('id', 'CHECK')

    def registration(self):
        return self.get_user_info('id', 'REGISTRATION')

    def regist_info_name(self):
        return self.get_user_info('xpath', 'NAME')

    def regist_info_lastname(self):
        return self.get_user_info('xpath', 'LASTNAME')

    def regist_address(self):
        return self.get_user_info('id', 'ADDRESS')

    def regist_pass(self):
        return self.get_user_info('id', 'PASS_CONF')

    def regist_btn(self):
        return self.get_user_info('xpath', 'REG_BTN')

    def link(self):
        return self.get_user_info('xpath', 'LINK')

    def rec_btn(self):
        return self.get_user_info('id', 'RECOVERY')

    def con_btn(self):
        return self.get_user_info('id', 'CONT_BTN')

    def choose_btn(self):
        return self.get_user_info('xpath', 'CHOOSE')

    def choose_btn_2(self):
        return self.get_user_info('xpath', 'CHOOSE_2')

    def get_new_pass(self):
        return self.get_user_info('id', 'NEW_PASS')

    def save_btn(self):
        return self.get_user_info('id', 'SAVE_BTN')

    def con_btn2(self):
        return self.get_user_info('xpath', 'CONT_2')

    def odn_btn(self):
        return self.get_user_info('id', 'ODN_BTN')

    def odn_log(self):
        return self.get_user_info('id', 'LOG_ODN')

    def odn_pass(self):
        return self.get_user_info('id', 'PASS_ODN')

    def enter_btn(self):
        return self.get_user_info('xpath', 'ENTER_ODN')

    def mail_btn(self):
        return self.get_user_info('id', 'MAIL_BTN')

    def enter_mail(self):
        return self.get_user_info('xpath', 'ENTER_MAIL')

    def log_mail(self):
        return self.get_user_info('id', 'LOG_MAIL')

    def ya_btn(self):
        return self.get_user_info('id', 'YA_BTN')

    def log_ya(self):
        return self.get_user_info('id', 'LOG_YA')

    def enter_ya(self):
        return self.get_user_info('xpath', 'ENTER_YA')

    def pass_ya(self):
        return self.get_user_info('xpath', 'YA_PASS')

    def select(self):
        return self.get_user_info('id', 'SELECT')
