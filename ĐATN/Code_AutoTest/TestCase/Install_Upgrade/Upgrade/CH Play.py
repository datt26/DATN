import time
import pytest
from appium import webdriver


###
# TC: KIỂM TRA CẬP NHẬT GAME TRÊN GOOGLE PLAY:
class TestUpdate:

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
        # 1. Tiến hành vào CH Play.
        element = self.driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Cửa hàng Play"]')
        element.click()
        time.sleep(2)

        # 2. Click vào phần tử "Tìm kiếm".
        element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Button")
        element.click()

        # 3. Điền từ khóa vào ô tìm kiếm.
        element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.EditText")
        element.send_keys('tic tac toe wintrino')
        self.driver.press_keycode(66) # gõ phím Enter

        # 4. Click vào kết quả tìm kiếm.
        element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]")
        element.click()
        time.sleep(2)

        # 5. Click vào button "Cập nhật":
        element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button[2]")
        element.click()
        time.sleep(2)


    	# Expect Result:
		# Hiển thị và cho phép người chơi cập nhật game thông qua tìm kiếm trên google play.
        # Dữ liệu game vẫn được lưu trữ.

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

if __name__ == '__main__':
    pytest.main(['CH Play.py'])