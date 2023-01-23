import pytest
from settings import Data
from autorization_part import Selecting
import time


@pytest.mark.usefixtures('setup')
class TestRegistration:
    """Регистрация через мобильный телефон"""

    def test_01(self):
        auto_1 = Selecting(self.driver)
        auto_1.registration().click()
        auto_1.regist_info_name().send_keys(Data.get('Имя'))
        auto_1.regist_info_lastname().send_keys(Data.get('Фамилия'))
        auto_1.regist_address().send_keys(Data.get('Мобильный телефон'))
        auto_1.get_password().send_keys(Data.get('Валидный пароль'))
        auto_1.regist_pass().send_keys(Data.get('Валидный пароль'))
        auto_1.regist_btn().click()

        try:
            assert auto_1.check_autho_page().text == 'Регистрация'
        finally:
            assert auto_1.acc_are().text == 'Учётная запись уже существует'

    """Регистрация через адрес электронной почты"""
    def test_02(self):
        auto_1 = Selecting(self.driver)
        auto_1.registration().click()
        auto_1.regist_info_name().send_keys(Data.get('Имя'))
        auto_1.regist_info_lastname().send_keys(Data.get('Фамилия'))
        auto_1.regist_address().send_keys(Data.get('Электронная почта'))
        auto_1.get_password().send_keys(Data.get('Валидный пароль'))
        auto_1.regist_pass().send_keys(Data.get('Валидный пароль'))
        auto_1.regist_btn().click()

        try:
            assert auto_1.check_autho_page().text == 'Регистрация'
        finally:
            assert auto_1.acc_are().text == 'Учётная запись уже существует'


@pytest.mark.usefixtures('setup')
class TestAuthorisation:

    """Авторизация через номер телефона"""

    def test_03(self):
        auto_1 = Selecting(self.driver)
        auto_1.get_log_field().send_keys(Data.get('Мобильный телефон'))
        auto_1.get_password().send_keys(Data.get('Валидный пароль'))
        time.sleep(30)  # Вводим символы с капчи, если нужно
        auto_1.auto_btn().click()
        assert auto_1.checking().text == 'Личный кабинет'

    """Авторизация через адрес электронной почты"""

    def test_04(self):
        auto_1 = Selecting(self.driver)
        auto_1.get_log_field().send_keys(Data.get('Электронная почта'))
        auto_1.get_password().send_keys(Data.get('Валидный пароль'))
        time.sleep(30)  # Вводим символы с капчи, если нужно
        auto_1.auto_btn().click()
        assert auto_1.checking().text == 'Личный кабинет'

    """Авторизация через логин"""

    def test_05(self):
        auto_1 = Selecting(self.driver)
        auto_1.get_log_field().send_keys(Data.get('Логин'))
        auto_1.get_password().send_keys(Data.get('Валидный пароль'))
        time.sleep(30)  # Вводим символы с капчи, если нужно
        auto_1.auto_btn().click()
        assert auto_1.checking().text == 'Личный кабинет'

    """Авторизация через социальную сеть 'Одноклассники'"""

    def test_06(self):
        auto_1 = Selecting(self.driver)
        auto_1.odn_btn().click()
        auto_1.odn_log().send_keys(Data.get('Мобильный телефон'))
        auto_1.odn_pass().send_keys(Data.get('Валидный пароль'))
        auto_1.enter_btn().click()
        assert auto_1.checking().text == 'Личный кабинет'

    """Авторизация через социальную сеть 'Мой Мир'"""

    def test_07(self):
        auto_1 = Selecting(self.driver)
        auto_1.mail_btn().click()
        auto_1.log_mail().send_keys(Data.get('Почтовый ящик'))
        auto_1.get_password().send_keys(Data.get('Пароль от почтового ящика'))
        auto_1.enter_mail().click()
        assert auto_1.checking().text == 'Личный кабинет'

    """Авторизация через социальную сеть 'Яндекс'"""

    def test_08(self):
        auto_1 = Selecting(self.driver)
        auto_1.ya_btn().click()
        auto_1.log_ya().send_keys(Data.get('Логин от янд'))
        auto_1.enter_ya().click()
        auto_1.pass_ya().send_keys(Data.get('Пароль от янд'))
        auto_1.enter_ya().click()
        assert auto_1.checking().text == 'Личный кабинет'


@pytest.mark.usefixtures('setup')
class TestRecoveryPass:
    """Восстановление пароля через номер телефона"""

    def test_09(self):
        auto_1 = Selecting(self.driver)
        auto_1.rec_btn().click()
        auto_1.get_log_field().send_keys(Data.get('Мобильный телефон'))
        time.sleep(30)  # время для заполнения капчи
        auto_1.con_btn().click()
        auto_1.choose_btn().click()
        auto_1.con_btn2().click()
        time.sleep(30)  # время для ввода кода
        auto_1.get_new_pass().send_keys(Data.get('Новый пароль'))
        auto_1.regist_pass().send_keys(Data.get('Новый пароль'))
        auto_1.save_btn().click()
        assert auto_1.checking().text == 'Личный кабинет'

    """Восстановление пароля через электронную почту"""

    def test_10(self):
        auto_1 = Selecting(self.driver)
        auto_1.rec_btn().click()
        auto_1.get_log_field().send_keys(Data.get('Электронная почта'))
        time.sleep(30)  # время для заполнения капчи
        auto_1.con_btn().click()
        auto_1.choose_btn_2().click()
        auto_1.con_btn2().click()
        time.sleep(30)  # время для ввода кода
        auto_1.get_new_pass().send_keys(Data.get('Новый пароль'))
        auto_1.regist_pass().send_keys(Data.get('Новый пароль'))
        auto_1.save_btn().click()
        assert auto_1.checking().text == 'Личный кабинет'

    """Проверка ссылки на пользовательское соглашение"""

    def test_11(self):
        auto_1 = Selecting(self.driver)
        auto_1.link().click()

        def scroll_down(offset=0):
            if offset:
                self.driver.execute_script('window.scrollTO(0, {0});'.format(offset))
            else:
                self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            return scroll_down()

        win_title = auto_1.driver.execute_script("return window.document.title")

        assert win_title == 'Ростелеком ID'


@pytest.mark.usefixtures('setup')
class TestStress:

    """Регистрация через мобильный телефон с паролем, короче 8 символов"""
    def test_12(self):
        auto_1 = Selecting(self.driver)
        auto_1.registration().click()
        auto_1.regist_info_name().send_keys(Data.get('Имя'))
        auto_1.regist_info_lastname().send_keys(Data.get('Фамилия'))
        auto_1.regist_address().send_keys(Data.get('Мобильный телефон'))
        auto_1.get_password().send_keys(Data.get('Короткий пароль'))
        auto_1.regist_pass().send_keys(Data.get('Короткий пароль'))
        auto_1.regist_btn().click()

        assert auto_1.error_regist().text == 'Длина пароля должна быть не менее 8 символов' or 'Пароли не совпадают'

    """Регистрация через мобильный телефон с паролем больше 255 символов"""
    def test_13(self):
        auto_1 = Selecting(self.driver)
        auto_1.registration().click()
        auto_1.regist_info_name().send_keys(Data.get('Имя'))
        auto_1.regist_info_lastname().send_keys(Data.get('Фамилия'))
        auto_1.regist_address().send_keys(Data.get('Мобильный телефон'))
        auto_1.get_password().send_keys(Data.get('Длинный пароль'))
        auto_1.regist_pass().send_keys(Data.get('Длинный пароль'))
        auto_1.regist_btn().click()

        assert auto_1.error_regist().text == 'Длина пароля должна быть не более 20 символов'

@pytest.mark.usefixtures('setup')
class TestNegative:

    """Авторизация с невалидным номером телефона"""

    def test_14(self):
        auto_1 = Selecting(self.driver)
        auto_1.get_log_field().send_keys(Data.get('Невалидный номер телефона'))
        auto_1.get_password().send_keys(Data.get('Валидный пароль'))
        #time.sleep(30)  # Вводим символы с капчи, если нужно
        auto_1.auto_btn().click()
        try:
            assert auto_1.error_check().text == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'
        except:
            assert auto_1.error_mess().text == 'Введите номер телефона' or 'Неверный формат телефона'

    """Авторизация с невалидным адресом электронной почты"""

    def test_15(self):
        auto_1 = Selecting(self.driver)
        auto_1.get_log_field().send_keys(Data.get('Невалидная электронная почта'))
        auto_1.get_password().send_keys(Data.get('Валидный пароль'))
        time.sleep(30)  # Вводим символы с капчи, если нужно
        auto_1.auto_btn().click()

        try:
            assert auto_1.error_check().text == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'

        except:
            assert auto_1.error_mess().text == 'Введите номер телефона' or 'Неверный формат телефона'

    """Авторизация с невалидным логином"""

    def test_16(self):
        auto_1 = Selecting(self.driver)
        auto_1.get_log_field().send_keys(Data.get('Невалидный логин'))
        auto_1.get_password().send_keys(Data.get('Валидный пароль'))
        time.sleep(30)  # Вводим символы с капчи, если нужно
        auto_1.auto_btn().click()

        try:
            assert auto_1.error_check().text == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'

        except:
            assert auto_1.error_mess().text == 'Введите номер телефона' or 'Неверный формат телефона'

    """Авторизация с невалидным номером лицевого счёта"""

    def test_17(self):
        auto_1 = Selecting(self.driver)
        auto_1.select().click()
        auto_1.get_log_field().send_keys(Data.get('Невалидный номер лицевого счёта'))
        auto_1.get_password().send_keys(Data.get('Валидный пароль'))
        time.sleep(30)  # Вводим символы с капчи, если нужно
        auto_1.auto_btn().click()

        try:
            assert auto_1.error_check().text == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'
        except:
            assert auto_1.error_mess().text == 'Введите номер телефона' or 'Неверный формат телефона'

    """Авторизация с логином, написанным верхним регистром"""

    def test_18(self):
        auto_1 = Selecting(self.driver)
        auto_1.get_log_field().send_keys(Data.get('Валидный логин ВР'))
        auto_1.get_password().send_keys(Data.get('Валидный пароль'))
        time.sleep(30)  # Вводим символы с капчи, если нужно
        auto_1.auto_btn().click()

        try:
            assert auto_1.error_check().text == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'
        except:
            assert auto_1.error_mess().text == 'Введите номер телефона' or 'Неверный формат телефона'

    """Авторизация с невалидным паролем"""
    def test_19(self):
        auto_1 = Selecting(self.driver)
        auto_1.get_log_field().send_keys(Data.get('Мобильный телефон'))
        auto_1.get_password().send_keys(Data.get('Невалидный пароль'))
        time.sleep(30)  # Вводим символы с капчи, если нужно
        auto_1.auto_btn().click()
        assert auto_1.error_check().text == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'

