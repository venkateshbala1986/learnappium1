import unittest
from set_up1 import set_up1
import random

class permission(set_up1):
    def test01_deny_permission(self):
         self.driver.reset()
         self.driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button").click()
         self.driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button").click()
         self.driver.launch_app()

    def test02_deny_permission(self):
        self.driver.reset()
        self. driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button").click()
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.launch_app()


    def test03_allow_permission(self):
        self.driver.reset()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.launch_app()


    def test04_onboarding(self):
        self.driver.reset()
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

        exp_result='Engaging videos that make learning simple and fun'
        some_result=self.driver.find_element_by_id("com.byjus.thelearningapp:id/textViewDetail")
        some_result1=some_result.get_attribute('text')
        print(some_result1)
        some_result2=some_result1.split()
        print(some_result2)
        actual_result=' '.join(some_result2)
        print(actual_result)
        assert exp_result in actual_result
        size = self.driver.get_window_size() #Horizontal scrolling the screen
        startx = int(size["width"] * 0.90)
        starty = int(size["height"] * 0.50)
        endx = int(size["width"] * 0.10)
        self.driver.swipe(startx, starty, endx, 1000)


        exp_result1='Unique learning journeys created just for you!'
        r=self.driver.find_element_by_id("com.byjus.thelearningapp:id/textViewDetail").get_attribute('text')
        print(r)
        r1=r.split()
        print(r1)
        actual_result1=' '.join(r1)
        print(actual_result1)
        assert exp_result1 in actual_result1
        size = self.driver.get_window_size() #Horizontal scrolling the screen
        startx = int(size["width"] * 0.90)
        starty = int(size["height"] * 0.50)
        endx = int(size["width"] * 0.10)
        self.driver.swipe(startx, starty, endx, 1000)

        exp_result2='Customized feedback with recommendations at every step'
        r2=self.driver.find_element_by_id("com.byjus.thelearningapp:id/textViewDetail").get_attribute('text')
        print(r2)
        r3=r2.split()
        print(r3)
        actual_result2=' '.join(r3)
        print(actual_result2)
        assert  exp_result2 in actual_result2
        self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonGetStarted").click()

        # self.driver.find_element_by_id("com.byjus.thelearningapp:id/tvRegister").click()
        # self.driver.find_element_by_id("com.byjus.thelearningapp:id/btnCohort").click()

    def test05_onboarding01(self):
        self.driver.reset()
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        try: #Exception handling
            while self.driver.find_element_by_xpath("//*[@text='Next']").is_displayed(): #While loop iteration using "is_displayed method"
                size = self.driver.get_window_size() #To scroll the screen horizontally
                startx = int(size["width"] * 0.90)
                starty = int(size["height"] * 0.50)
                endx = int(size["width"] * 0.10)
                self.driver.swipe(startx, starty, endx, 1000)
        except:
            self.driver.find_element_by_xpath("//*[@text='Get Started']").click()

    # def test05_registration_negative(self):
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/etPhoneNumber").clear()
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/tvRegister").click()
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/btnCohort").click()
    #
    #     exp_text = "Please enter your name." # Validation for name field
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/btnRegister").click()
    #     error_name = self.driver.find_element_by_xpath(
    #         "//*[@resource-id='com.byjus.thelearningapp:id/layoutName']//*[@resource-id='com.byjus.thelearningapp:id/textinput_error']")
    #     actual_text = error_name.get_attribute('text')
    #     print(actual_text)
    #     assert exp_text in actual_text
    #
    #     exp_text="Please enter your mobile number" # Validation for mobile number field
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/tvPhoneError").clear()
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/btnRegister").click()
    #     error_number=self.driver.find_element_by_xpath(
    #         "//*[@resource-id='com.byjus.thelearningapp:id/layoutPhoneNumber']//*[@resource-id='com.byjus.thelearningapp:id/tvPhoneError']")
    #     actual_text=error_number.get_attribute('text')
    #     print(actual_text)
    #     assert exp_text in actual_text
    #
    #     exp_text="Please enter your email address" #Validation for email id field
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/btnRegister").click()
    #     error_email = self.driver.find_element_by_xpath(
    #         "//*[@resource-id='com.byjus.thelearningapp:id/layoutEmail']//*[@resource-id='com.byjus.thelearningapp:id/textinput_error']")
    #     actual_text=error_email.get_attribute('text')
    #     print (actual_text)
    #     assert exp_text in actual_text
    #
    #     exp_text="Please enter your city" #Validation for city field
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/etCity").clear()
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/btnRegister").click()
    #     error_city=self.driver.find_element_by_xpath(
    #         "//*[@resource-id='com.byjus.thelearningapp:id/layoutLocation']//*[@resource-id='com.byjus.thelearningapp:id/textinput_error']")
    #     actual_text=error_city.get_attribute('text')
    #     print(actual_text)
    #     assert  exp_text in actual_text
    #
    #     print("Negative test cases for registration executed successfully")
    #
    # def test06_registration_positive(self):
    #     self.driver.implicitly_wait(90)
    #     #self.driver.find_element_by_id("com.byjus.thelearningapp:id/buttonSkip").click()
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/tvRegister").click()
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/btnCohort").click()
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/etName").send_keys("swami")
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/etPhoneNumber").clear()
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/etPhoneNumber").send_keys(random.randint(1000000000,9999999999)) # Generate random mobile number
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/etEmail").send_keys("qwert@gmail.com")
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/etCity").clear()
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/etCity").send_keys("che")
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/etName").click()
    #     self.driver.implicitly_wait(30)
    #     self.driver.find_element_by_id("com.byjus.thelearningapp:id/btnRegister").click()
    #     self.driver.implicitly_wait(30)
    #     self.driver.find_element_by_xpath("//*[@resource-id='com.byjus.thelearningapp:id/layoutPhoneNumber']").send_keys(1234)
    #     print("Positive test cases for registration executed successfully")








if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(permission)
    unittest.TextTestRunner(verbosity=2).run(suite)






