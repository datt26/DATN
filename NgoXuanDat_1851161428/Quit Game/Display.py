
from appium import webdriver 
import tkinter.messagebox 

desired_cap = {
 	"uuid": "emulator-5554", 
 	"platformName": "Android",
 	"platformVersion": "9", 
 	"app": "D:/@Documents/DO_AN_TOT_NGHIEP/SETUP/Tic Tac Toe_v8.0.60_apkpure.apk",
 	"noReset": "true" 
 }

###
# TC: KIỂM TRA HIỂN THỊ GIAO DIỆN QUIT GAME:

# Steps 1:
# Kết nối thành công
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Steps 2:
# Tiến hành vào game 

# Steps 3:
# Nhấn nút back trên thiết bị.
driver.press_keycode(4)

# Expect Result:
# Khi nhấn nút back trên thiết bị, màn hình cảnh báo thoát game sẽ xuất hiện.
# Màn hình phải hiển thị 2 lựa chọn: "Yes" và "No" cho người chơi.
