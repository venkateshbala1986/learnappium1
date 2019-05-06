import os
import unittest
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By





class set_up1(unittest.TestCase):
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
    @classmethod # @classmethod annotation should be given on top of class function, if the function belongs to the class
    def tearDown(cls):
        cls.driver.quit()





if __name__ == '__main__': #Main method
    suite = unittest.TestLoader().loadTestsFromTestCase(set_up1)
    unittest.TextTestRunner(verbosity=2).run(suite)