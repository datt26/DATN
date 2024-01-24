import time
import pytest
from appium import webdriver


###
# TC: KIỂM TRA CHECK BOX LEVEL CHƠI Ở CHẾ ĐỘ CHƠI ĐƠN:
class TestCheckboxLevel:

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
    	# Click vào các check box level.
    	# Hard:
    	element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[8]/android.widget.Image")
    	element.click()
    	time.sleep(2)

    	# Expert:
    	element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[11]/android.widget.Image")
    	element.click()
    	time.sleep(2)

    	# Medium:
    	element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[5]/android.widget.Image")
    	element.click()
    	time.sleep(2)

    	# Easy:
    	element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.Image")
    	element.click()
    	time.sleep(5)

    	# Expect Result:
		# Các checkbox được thực hiện đúng thao tác và Chỉ được chọn một giá trị duy nhất.
		# Hiển thị pop-up thông báo.

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

if __name__ == '__main__':
    pytest.main(['Checkbox_level.py'])