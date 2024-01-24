import time
import pytest
from appium import webdriver


###
# TC: KIỂM TRA BUTTON "YES" Ở GIAO DIỆN QUIT GAME:
class TestButtonYES:

    @classmethod
    def setup_class(cls):
        desired_caps = {
            "uuid": "emulator-5554", 
 			"platformName": "Android",
 			"platformVersion": "9", 
 			"app": "D:/@Documents/DO_AN_TOT_NGHIEP/SETUP/Tic Tac Toe_v8.0.60_apkpure.apk",
 			"noReset": "true"
        }

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def test_example(self):
        # Test Steps:
    	# Nhấn nút back trên thiết bị.
        self.driver.press_keycode(4)
        time.sleep(2)

        # Click vào button "Yes".
        element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]")
        element.click()
        time.sleep(2)

    	# Expect Result:
		# Khi click vào button "Yes", game thoát thành công.

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

if __name__ == '__main__':
    pytest.main(['button_YES.py'])