
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
# TC: KIỂM TRA TICK VÀO CHECKBOX "DON'T ASK AGAIN" Ở GIAO DIỆN QUIT GAME:

# Steps 1:
# Kết nối thành công
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Steps 2:
# Tiến hành vào game 

# Steps 3:
# Nhấn nút back trên thiết bị.
driver.press_keycode(4)

# Steps 4:
# Click vào checkbox "Don't ask again".
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View[8]/android.widget.Image")
element.click()

# Expect Result:
# Khi tick vào checkbox "Don't ask again" <=> Bỏ tick checkbox "Quit game warning" ở giao diện Setting.
# Checkbox "Quit game warning" ở giao diện Setting được bỏ tick. (Kiểm tra TC Setting ở mục GUI)
# Màn hình cảnh báo thoát game không xuất hiện khi quit game. (Kiểm tra TC Display)