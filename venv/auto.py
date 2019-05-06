import os
import unittest
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class auto(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'Pixel_XL_API_27'
        desired_caps['noReset'] = 'true'
        desired_caps['app'] = PATH('D:\Downloads\BYJUS.apk')
        desired_caps['appPackage'] = 'com.byjus.thelearningapp'
        desired_caps['appActivity'] = 'com.byjus.app.onboarding.activity.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def tearDown(self):
             self.driver.quit()

    # def test01_onboarding(self):
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_element_by_android_uiautomator('new UiSelector().text("Next")').click()
    #     self.driver.find_element_by_android_uiautomator('new UiSelector().text("Next")').click()
    #     self.driver.find_element_by_android_uiautomator('new UiSelector().text("Get Started")').click()
    #     self.driver.find_element_by_android_uiautomator('new UiSelector().text("8th")').click()
    #     self.driver.find_element_by_android_uiautomator('new UiSelector().text("Login")').click()
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/etPhoneNumber").send_keys(1102104000)
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/btnLogin").click()#tap on "next" button
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/etOTP").send_keys(1234)
    #     self.driver.implicitly_wait(20)

    def test02_homescreen(self):
         self.driver.implicitly_wait(60)
         self.driver.find_element_by_xpath("//*[@resource-id='com.byjus.thelearningapp:id/home_subject_cardview']//*[@text='Mathematics']").click()
         # size=self.driver.get_window_size()
         # starty = int(size["height"] * 0.90)
         # endy = int(size["height"] * 0.20)
         # startx = int(size["width"] * 0.50)
         # sleep(10)
         # self.driver.swipe(startx,starty,startx,endy,3000)
         # sleep(5)
         # self.driver.swipe(startx, starty, startx, endy, 3000)
         # el2 = self.driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc='TODO'])[2]").click()
         # self.driver.scroll(el1, el2)
         #self.driver.find_element_by_android_uiautomator('text("Numbers and Its Properties")').click()
         self.driver.find_element_by_xpath(
             "//*[@resource-id='com.byjus.thelearningapp:id/parent_layout']//*[@text='Numbers and Its Properties']").click()
         sleep(5)
         self.driver.find_element_by_xpath("//android.widget.Button[@text='Next']").click()
         self.driver.back()
         size = self.driver.get_window_size()
         starty = int(size["height"] * 0.90)
         endy = int(size["height"] * 0.20)
         startx = int(size["width"] * 0.50)
         sleep(10)
         self.driver.swipe(startx, starty, startx, endy, 3000)
         self.driver.implicitly_wait(40)
         self.driver.find_element_by_id("com.byjus.thelearningapp:id/btnPositive").click()
         self.driver.implicitly_wait(80)
         self.driver.find_element_by_xpath(
             "//*[@resource-id='com.byjus.thelearningapp:id/action_button_tray']//*[@resource-id='com.byjus.thelearningapp:id/action_morph_btn']").click()
         self.driver.implicitly_wait(60)
         self.driver.find_element_by_xpath("//android.view.View[@content-desc='the same integer']").click()
         self.driver.find_element_by_xpath("//android.view.View[@content-desc='Submit']").click()
         self.driver.find_element_by_xpath("//android.view.View[@content-desc='Next']").click()





         # self.driver.implicitly_wait(30)
         #
         #
         #
         # self.driver.find_element_by_accessibility_id('android:id/content').click()
         # self.driver.implicitly_wait(20)
         # self.driver.find_element_by_android_uiautomator(text('Next')).click()
         # self. driver.find_element_by_xpath('//android.view.View[@index=2]').click()
         # self.driver.find_element_by_accessibility_id(text('Submit')).click()
         # self.driver.find_element_by_accessibility_id(text('Next')).click()








    # def test_verify_my_text(self):
    #         self.driver.implicitly_wait(10)
    #         str1 = "SKIP"
    #         # str2=self.driver.find_element_by_link_text("SKIP")
    #         ele = self.driver.find_element_by_android_uiautomator('new UiSelector().text("SKIP")')
    #         str2 = ele.text
    #         print(str1)
    #         print(str2)
    #         if str1 == str2:
    #             print("Skip text is present")
    #             sleep(2)
    #             ele.click()
    #             sleep(10)
    #         else:
    #             print("strings are not equal")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(auto)
    unittest.TextTestRunner(verbosity=2).run(suite)


