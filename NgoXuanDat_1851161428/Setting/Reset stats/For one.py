
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
# TC: KIỂM TRA BUTTON "RESET STATS FOR ONE PLAYER" Ở GIAO DIỆN SETTING:

# Steps 1:
# Kết nối thành công
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Steps 2:
# Tiến hành vào game 

# Steps 3:
# Đóng màn hình Welcome

# Steps 4:
# Click vào button "SETT" ở màn hình GUI.
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[1]/android.view.View/android.view.View[5]/android.widget.Image")
element.click()

# Steps 5:
# Click vào button "Reset stats for one player".
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View[10]")
element.click()

# Expect Result:
# Khi click vào button, các bản ghi số liệu trong phần Statistics của chế độ chơi đơn sẽ được reset về 0.
# Xuất hiện thông báo thực hiện thành công.