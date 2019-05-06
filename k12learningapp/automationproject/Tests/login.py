import os
import unittest
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import random
# from k12learningapp.automationproject.Pages.permissions import Permissions
# from k12learningapp.automationproject.Pages.onboarding import Onboarding
from k12learningapp.automationproject.Pages.loginscreen import LoginScreen



class login(unittest.TestCase):
    @classmethod # @classmethod annotation should be given on top of class function, if the function belongs to the class
    def setUp(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'Pixel_XL_API_27'
        desired_caps['noReset'] = 'true'
        desired_caps['app'] ='D:\Downloads\BYJUS.apk'
        desired_caps['appPackage'] = 'com.byjus.thelearningapp'
        desired_caps['appActivity'] = 'com.byjus.app.onboarding.activity.SplashActivity'

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(30)



    def test_login(self):
        # self.driver.reset()
        driver=self.driver
        # permission=Permissions(driver)  #Creating object using other page classname
        # permission.launch_deny_permission() #Calling action/function from other page class
        # permission.deny_permission()
        # permission.launch_permission()
        #
        #
        # onboarding=Onboarding(driver)
        # onboarding.launch_onboarding()

        login=LoginScreen(driver)
        login.enter_phonenumber("1102104001")
        login.click_next()
        self.driver.implicitly_wait(20)
        login.enter_otp("1234")


    @classmethod  # @classmethod annotation should be given on top of class function, if the function belongs to the class
    def tearDownClass(cls):
        cls.driver.quit()





if __name__ == '__main__': #Main method
    suite = unittest.TestLoader().loadTestsFromTestCase(login)
    unittest.TextTestRunner(verbosity=2).run(suite)