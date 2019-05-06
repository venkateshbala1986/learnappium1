

class LoginScreen():
    phonenumber_textbox_id=None
    next_button_id=None
    otp_field_id=None

    def __init__(self,driver):  # constructor
        self.driver = driver  # creating variables for locators
        self.phonenumber_textbox_id="com.byjus.thelearningapp:id/etPhoneNumber"
        self.next_button_id="com.byjus.thelearningapp:id/btnLogin"
        self.otp_field_id="com.byjus.thelearningapp:id/etOTP"


    def enter_phonenumber(self,phonenumber): #creating actions/functions for locators
        self.driver.find_element_by_id(self.phonenumber_textbox_id).clear()# Apply condition if number is present, then clear& assertion
        self.driver.find_element_by_id(self.phonenumber_textbox_id).send_keys(phonenumber) #Add Otp screen locators


    def click_next(self):
        self.driver.find_element_by_id(self.next_button_id).click() # perform some login test cases of manual and rearrange the hierarchy of the project

    def enter_otp(self,otp):
         self.driver.find_element_by_id(self.otp_field_id).send_keys(otp)