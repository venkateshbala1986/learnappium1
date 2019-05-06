import os
import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class practice(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'device'
        desired_caps['noReset'] = 'true'
        desired_caps['app'] = PATH('D:\..\..\..\Downloads\BYJUS.apk')
        desired_caps['appPackage'] = 'com.byjus.thelearningapp'
        desired_caps['appActivity'] = 'com.byjus.app.registration.activity.OnBoardingActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()


    def test01_permission(self):
         self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click() # find an element by "resourceid"
         self.driver.find_element_by_xpath("//android.widget.Button[@text='DENY']").click() # find an element by "xpath "
         self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
         self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
         self.driver.implicitly_wait(10)
         self.driver.find_element_by_android_uiautomator('new UiSelector().text("SKIP")').click()
         self.driver.implicitly_wait(10)
         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/course_name_view")').click()
         self.driver.implicitly_wait(10)
         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/full_name_main_view")').send_keys("swami")
         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/phone_number_view")').send_keys(2307213457) #Mobile number should be dynamic
         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/email_view")').send_keys("swami12345@gmail.com")
         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/city_view")').click()
         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/register_button_view")').click()
         self.driver.implicitly_wait(10)
         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/dialog_otp_verify_edttxt_otp")').send_keys("1234")
         self.driver.implicitly_wait(10)

    def test01_login(self):
         self.driver.find_element_by_android_uiautomator('new UiSelector().text("Allow")').click() #find an element by "resourceid"
         self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
         self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
         self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
         self.driver.implicitly_wait(10)
         self.driver.find_element_by_android_uiautomator('new UiSelector().text("SKIP")').click() #find an element by "text"
         self.driver.implicitly_wait(10)
         self.driver.find_element_by_id ("com.byjus.thelearningapp:id/course_name_view").click() #find an element by "resourceid"
         self.driver.implicitly_wait(10)
         self.driver.find_element_by_id("com.byjus.thelearningapp:id/login_button").click()
         self.driver.implicitly_wait(10)
         self.driver.find_element_by_id("com.byjus.thelearningapp:id/top_text_view").send_keys(8095704055)
         #element(by.id('foo')).send_Keys('bar');
         self.driver.implicitly_wait(10)
         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/btn_login")').click()
         self.driver.implicitly_wait(10)
         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/edttxt_password")').send_keys(123456)
         self.driver.implicitly_wait(10)
         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/btn_login")').click()
         sleep(10)
         self.driver.implicitly_wait(10)
         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/roundedNavButton")').click()
         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/home_drawer_imgvw_arrow_right")').click()
         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/tvGrade")').click()
         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/course_view_group")').click()
         self.driver.implicitly_wait(10)
         sleep(10)

         size = self.driver.get_window_size() #swipe from down to up
         starty = int(size["height"] * 0.90)
         endy = int(size["height"] * 0.20)
         startx = int(size["width"] * 0.50)
         sleep(2)
         self.driver.swipe(startx, starty, startx, endy, 1000)
         #actions = TouchAction(driver)
         #actions.scroll_from_element(element,100,100)
         #actions.scroll(100,100)
         #actions.perform()
         self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/signout")').click()
         self.driver.implicitly_wait(10)


    #def test02_gradeProfile(self):
        #self.driver.implicitly_wait(10)
        #self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/roundedNavButton")').click()
        #self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/home_drawer_imgvw_arrow_right")').click()
        #self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/tvGrade")').click()
        #self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/course_view_group")').click()
        #self.driver.implicitly_wait(10)
        #sleep(10)
        #actions = TouchAction(driver)
        #actions.scroll_from_element(element, 10, 100)
        #actions.scroll(10, 100)
        #actions.perform()
        #self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.byjus.thelearningapp:id/signout")').click()
        #self.driver.implicitly_wait(10)




'''
    def test_verify_my_text(self):
        self.driver.implicitly_wait(10)
        str1= "SKIP"
        #str2=self.driver.find_element_by_link_text("SKIP")
        ele=self.driver.find_element_by_android_uiautomator('new UiSelector().text("SKIP")')
        str2=ele.text
        print(str1)
        print(str2)
        if str1==str2:
            print("Skip text is present")
            sleep(2)
            ele.click()
            sleep(10)
        else:
            print("strings are not equal")

'''

if __name__ == '__main__': #Main function
    suite = unittest.TestLoader().loadTestsFromTestCase(practice)
    unittest.TextTestRunner(verbosity=2).run(suite)