import time
import pytest
from appium import webdriver


###
# TC: KIỂM TRA BUTTON "1 Players" Ở CHẾ ĐỘ MULTIPLAYER:
class TestButton1_Player:

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
    	# Click vào button "2 Players".
    	element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[1]/android.view.View/android.view.View[3]/android.widget.Image")
    	element.click()
    	time.sleep(2)

    	# Click vào button "1 Players".
    	element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[1]/android.view.View/android.view.View[3]/android.widget.Image")
    	element.click()
    	time.sleep(10)

    	# Expect Result:
		# Xuất hiện giao diện chế độ chơi đơn.
		# Xuất hiện pop-up thông báo chuyển chế độ chơi.

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

if __name__ == '__main__':
    pytest.main(['button_1Player.py'])