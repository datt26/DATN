import time
import pytest
from appium import webdriver


###
# TC: KIỂM TRA GAME ĐƯỢC QUẢNG CÁO Ở GIAO DIỆN STATISTIC:
class TestAdsGame:

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
    	# Click vào button "STATS" ở giao diện GUI.
    	element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Image")
    	element.click()
    	time.sleep(2)

    	# Click vào khu vực game được quảng cáo.
    	# Ads game 1:
    	element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View[7]/android.view.View/android.view.View/android.view.View[1]")
    	element.click()
    	time.sleep(5)

    	# Ads game 2:
    	# element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View[7]/android.view.View/android.view.View/android.view.View[2]")
    	# element.click()
    	# time.sleep(5)

    	# Expect Result:
		# Xuất hiện đúng tựa game mà nhà phát triển quảng cáo.

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

if __name__ == '__main__':
    pytest.main(['Ads.py'])