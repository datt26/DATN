
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
# TC: KIỂM TRA BUTTON "2 Players" Ở CHẾ ĐỘ CHƠI ĐƠN:

# Steps 1:
# Kết nối thành công
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
# Cài đặt thời gian chờ phần tử xuất hiện
driver.implicitly_wait(30)

# Steps 2:
# Tiến hành vào game 
#element = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Tic Tac Toe"]')
#element.click()


# Steps 3:
# Click vào button "OK"
#element = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View[7]')
#element.click()

# Steps 4:
# Click vào button "2 Players".
element = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[1]/android.view.View/android.view.View[3]/android.widget.Image')
element.click()

# Steps 5:
# Click vào button "1 Players".
element = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[1]/android.view.View/android.view.View[3]/android.widget.Image')
element.click()

# Expect Result:
# Xuất hiện giao diện chế độ Multiplayer.
# Xuất hiện pop-up thông báo chuyển chế độ chơi.