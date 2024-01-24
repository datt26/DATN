import time
import pytest
from appium import webdriver


###
# TC: KIỂM TRA ICON "SHARE" Ở GIAO DIỆN WELCOME:
class TestIconSHARE:

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

        # Click vào icon "Share":
        element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]")
        element.click()
        time.sleep(2)

        # Click vào ứng dụng để chia sẻ:
        element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
        element.click()
        time.sleep(5)

    	# Expect Result:
		# Xuất hiện màn hình Share và cho phép người dùng share game.

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

if __name__ == '__main__':
    pytest.main(['Share.py'])