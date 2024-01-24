import time
import pytest
from appium import webdriver


###
# TC: KIỂM TRA CHECKBOX "SOUND EFFECTS" Ở GIAO DIỆN SETTING:
class TestCheckBox:

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
    	# Click vào button "Sett" ở giao diện GUI.
    	element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[1]/android.view.View/android.view.View[5]/android.widget.Image")
    	element.click()
    	time.sleep(2)

    	# Click vào checkbox "Sound Effects".
    	element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View[9]/android.view.View/android.view.View/android.view.View[1]/android.widget.Image")
    	element.click()
    	time.sleep(5)

    	# Expect Result:
		# Checkbox được thực hiện đúng thao tác.
		# Xuất hiện pop-up thông báo.
		# Khi checkbox được chọn, các hiệu ứng âm thanh của game sẽ được bật và ngược lại.

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

if __name__ == '__main__':
    pytest.main(['Sound Effects.py'])