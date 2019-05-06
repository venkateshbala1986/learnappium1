import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class emulator(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '9.0'
        desired_caps['deviceName'] = 'Pixel API 28'
        desired_caps['app'] = PATH('D:\..\..\..\Downloads\BYJUS.apk')
        #desired_caps['appPackage'] = 'com.byjus.thelearningapp'
        #desired_caps['appActivity'] = 'com.byjus.app.registration.activity.OnBoardingActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_verify_my_text(self):
            self.driver.implicitly_wait(10)
            str1 = "SKIP"
            # str2=self.driver.find_element_by_link_text("SKIP")
            ele = self.driver.find_element_by_android_uiautomator('new UiSelector().text("SKIP")')
            str2 = ele.text
            print(str1)
            print(str2)
            if str1 == str2:
                print("Skip text is present")
                sleep(2)
                ele.click()
                sleep(10)
            else:
                print("strings are not equal")

if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(emulator)
        unittest.TextTestRunner(verbosity=2).run(suite)


