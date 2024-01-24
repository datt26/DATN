import time
import pytest
from appium import webdriver


###
# TC: KIỂM TRA LOGO NHÀ PHÁT TRIỂN Ở GIAO DIỆN WELCOME:
class TestLOGO:

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

        # Click vào "Logo" của nhà phát triển:
        element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View[8]")
        element.click()
        time.sleep(5)

    	# Expect Result:
		# Xuất hiện các thông tin liên quan của nhà phát triển.

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

if __name__ == '__main__':
    pytest.main(['Logo.py'])