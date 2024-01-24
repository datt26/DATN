import time
import pytest
from appium import webdriver


###
# TC: KIỂM TRA BUTTON "OK" Ở GIAO DIỆN WELCOME:
class TestButton_OK:

    @classmethod
    def setup_class(cls):
        desired_caps = {
            "uuid": "emulator-5554", 
 			"platformName": "Android",
 			"platformVersion": "9", 
 			"appPackage": "com.ldmnq.launcher3",
            "appActivity": "com.android.launcher3.Launcher",
 			"noReset": "true"
        }

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def test_example(self):
        # Test Steps:
        # Tiến hành vào game
        element = self.driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Tic Tac Toe"]')
        element.click()
        time.sleep(2)

        # Click vào button "OK":
        element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View[7]")
        element.click()
        time.sleep(5)


    	# Expect Result:
		# Tắt màn hình Welcom và Xuất hiện màn hình GUI.

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

if __name__ == '__main__':
    pytest.main(['OK.py'])