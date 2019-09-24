from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM= (By.CSS_SELECTOR, "login_form")

    REG_FORM= (By.CSS_SELECTOR, "register_form")

    MAIL=(By.CSS_SELECTOR,"#id_registration-email")
    
    PSWRD=(By.CSS_SELECTOR,"#id_registration-password1")

    PSWRD2=(By.CSS_SELECTOR,"#id_registration-password2")

    REG=(By.CSS_SELECTOR,"#register_form>.btn.btn-lg.btn-primary")

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class Locators():
    BSKT= (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket ")

    TXT=(By.CSS_SELECTOR, ".col-sm-6.product_main>h1")

    TXT2=(By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in>.alertinner>strong")

    SUC= (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success")

    CHECK_BSKT=(By.CSS_SELECTOR, ".btn-group>.btn.btn-default")

    TXT3=(By.CSS_SELECTOR, "#messages")

    BUY=(By.CSS_SELECTOR,".btn.btn-lg.btn-primary.btn-block")
