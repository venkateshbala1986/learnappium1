

class Onboarding():
    # next_button_xpath = None
    # get_started_button_xpath=None
    next_button_id=None
    getstarted_button_id=None

    def __init__(self, driver):  # constructor
        self.driver = driver
        # self.next_button_xpath ="//*[@text='Next']"
        # self.get_started_button_xpath="//*[@text='Get Started']"
        self.next_button_id="com.byjus.thelearningapp:id/textViewDetail"
        self.getstarted_button_id="com.byjus.thelearningapp:id/buttonGetStarted"

    def launch_onboarding(self):
        exp_result = 'Engaging videos that make learning simple and fun'
        some_result = self.driver.find_element_by_id(self.next_button_id)
        some_result1 = some_result.get_attribute('text')
        print(some_result1)
        some_result2 = some_result1.split()
        print(some_result2)
        actual_result = ' '.join(some_result2)
        print(actual_result)
        assert exp_result in actual_result
        size = self.driver.get_window_size()  # Horizontal scrolling the screen
        startx = int(size["width"] * 0.90)
        starty = int(size["height"] * 0.50)
        endx = int(size["width"] * 0.10)
        self.driver.swipe(startx, starty, endx, 1000)

        exp_result1 = 'Unique learning journeys created just for you!'
        r = self.driver.find_element_by_id(self.next_button_id).get_attribute('text')
        print(r)
        r1 = r.split()
        print(r1)
        actual_result1 = ' '.join(r1)
        print(actual_result1)
        assert exp_result1 in actual_result1
        size = self.driver.get_window_size()  # Horizontal scrolling the screen
        startx = int(size["width"] * 0.90)
        starty = int(size["height"] * 0.50)
        endx = int(size["width"] * 0.10)
        self.driver.swipe(startx, starty, endx, 1000)

        exp_result2 = 'Customized feedback with recommendations at every step'
        r2 = self.driver.find_element_by_id(self.next_button_id).get_attribute('text')
        print(r2)
        r3 = r2.split()
        print(r3)
        actual_result2 = ' '.join(r3)
        print(actual_result2)
        assert exp_result2 in actual_result2
        self.driver.find_element_by_id(self.getstarted_button_id).click()

        # try: #Exception handling
        #     while self.driver.find_element_by_xpath(next_button_xpath).is_displayed(): #While loop iteration using "is_displayed method"
        #         size = self.driver.get_window_size() #To scroll the screen horizontally
        #         startx = int(size["width"] * 0.90)
        #         starty = int(size["height"] * 0.50)
        #         endx = int(size["width"] * 0.10)
        #         self.driver.swipe(startx, starty, endx, 1000)
        # except:
        #     self.driver.find_element_by_xpath(get_started_button_xpath).click()




