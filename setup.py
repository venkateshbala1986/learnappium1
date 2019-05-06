import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'device'
        desired_caps['app'] = PATH('D:\..\..\..\Downloads\BYJUS.apk')
        desired_caps['appPackage'] = 'com.byjus.thelearningapp'
        desired_caps['appActivity'] = 'com.byjus.app.registration.activity.OnBoardingActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_add_contacts(self):
        self.driver.implicitly_wait(10)
        #self.driver.find_element_by_id('permission_allow_button').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Allow")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Deny")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Deny")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Deny")').click()

    def test_allow(self):
        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id('permission_allow_button').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Allow")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Allow")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Allow")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Allow")').click()

     def test_text(self):
         self.driver.implicitly_wait(10)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)