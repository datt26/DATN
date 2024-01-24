import time
import pytest
from appium import webdriver


###
# TC: KIỂM TRA HIỂN THỊ GIAO DIỆN QUIT GAME:
class TestDisplayQUIT:

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
    	# Nhấn nút back trên thiết bị.
        self.driver.press_keycode(4)
        time.sleep(5)

    	# Expect Result:
		# Khi nhấn nút back trên thiết bị, màn hình cảnh báo thoát game sẽ xuất hiện.
        # Màn hình phải hiển thị 2 lựa chọn: "Yes" và "No" cho người chơi.

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

if __name__ == '__main__':
    pytest.main(['Display.py'])