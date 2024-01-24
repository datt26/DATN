import time
import pytest
from appium import webdriver


###
# TC: KIỂM TRA CHECKBOX "DON'T SHOW AGAIN" Ở GIAO DIỆN WELCOME (SAU):
class TestCheckBox:

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
        time.sleep(5)

        # Click vào checkbox "Don"t show again":
        element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View[7]/android.widget.Image")
        element.click()
        time.sleep(5)


    	# Expect Result:
        # Màn hình Welcome không xuất hiện khi vào game. (Kiểm tra TC Start.py)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

if __name__ == '__main__':
    pytest.main(['show again.py'])