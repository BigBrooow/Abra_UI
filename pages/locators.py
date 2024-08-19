from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.XPATH, '//*[@id="root"]/div/div/div/form/div[1]/input')
    LOGIN_PASSWORD = (By.XPATH, '//*[@id="root"]/div/div/div/form/div[2]/input')
    LOGIN_BTN = (By.XPATH, '//*[@id="root"]/div/div/div/form/button')
    INVALID_PASSWORD = (By.XPATH, '//*[@id="root"]/div/div/div/form/div[2]/span')
    EMAIL_IS_REQUIRED = (By.XPATH, '//*[@id="root"]/div/div/div/form/div[1]/span')
    PASSWORD_IS_REQUIRED = (By.XPATH, '//*[@id="root"]/div/div/div/form/div[2]/span')
    PASSWORD_VISIBILITY = (By.XPATH, '//*[@id="root"]/div/div/div/form/div[2]/button')


class MainPageLocators:
    PROFILE_BTN = (By.XPATH, '//*[@id="root"]/div/div/header/div[1]/div/div[2]/div/button')
