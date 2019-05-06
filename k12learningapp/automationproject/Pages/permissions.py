





class Permissions():
     permission_allow_button_id=None  #Global variable
     permission_deny_button_id = None

     def __init__(self,driver):  #constructor
         self.driver=driver      #variables for locators
         self.permission_allow_button_id="com.android.packageinstaller:id/permission_allow_button" #Local variable
         self.permission_deny_button_id="com.android.packageinstaller:id/permission_deny_button"

     def launch_deny_permission(self):
         self.driver.reset()
         self.driver.find_element_by_id(self.permission_allow_button_id).click()
         self.driver.find_element_by_id(self.permission_deny_button_id).click()
         self.driver.launch_app()

     def deny_permission(self):
         self.driver.reset()
         self.driver.find_element_by_id(self.permission_deny_button_id).click()
         self.driver.find_element_by_id(self.permission_allow_button_id).click()
         self.driver.launch_app()

     def launch_permission(self):   #actions/functions for locators
         self.driver.reset()
         self.driver.find_element_by_id(self.permission_allow_button_id).click() # Replace element locators with variable
         self.driver.find_element_by_id(self.permission_allow_button_id).click()











