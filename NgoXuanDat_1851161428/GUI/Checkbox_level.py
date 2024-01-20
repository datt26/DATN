
from appium import webdriver 
import tkinter.messagebox 

desired_cap = {
 	"uuid": "emulator-5554", 
 	"platformName": "Android",
 	"platformVersion": "9", 
 	"app": "D:/@Documents/DO_AN_TOT_NGHIEP/SETUP/Tic Tac Toe_v8.0.60_apkpure.apk",
 	"noReset": "true"
 	#"appPackage": "com.ldmnq.launcher3", # tên gói dl của app
 	#"appActivity": "com.android.launcher3.Launcher" # tên hoạt động của app
 }

###
# TC: KIỂM TRA CHECK BOX LEVEL CHƠI Ở CHẾ ĐỘ CHƠI ĐƠN:


# Steps 1:
# Kết nối thành công
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
# Cài đặt thời gian chờ phần tử xuất hiện
driver.implicitly_wait(30)

# Steps 2:
# Tiến hành vào game 

# Steps 3:
# Đóng màn hình Welcome

# Steps 4:
# Click vào các check box level.
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[8]/android.widget.Image")
element.click()
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[11]/android.widget.Image")
element.click()
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[5]/android.widget.Image")
element.click()
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.Image")
element.click()

# Expect Result:
# Các checkbox được thực hiện đúng thao tác và Chỉ được chọn một giá trị duy nhất.
# Hiển thị pop-up thông báo.