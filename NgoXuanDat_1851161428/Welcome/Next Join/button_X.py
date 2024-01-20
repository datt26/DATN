#nhập thư viện appium
from appium import webdriver 

#Thông tin cần lấy 
desired_cap = {
 	"uuid": "emulator-5554", # id của thiết bị
 	"platformName": "Android",
 	"platformVersion": "9", 
 	"appPackage": "com.ldmnq.launcher3", 
 	"appActivity": "com.android.launcher3.Launcher",
 	"noReset": "true"
 }

###
# TC: KIỂM TRA BUTTON "X" Ở GIAO DIỆN WELCOME (SAU):

# Steps 1:
# Kết nối thành công
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Steps 2:
# Tiến hành vào game:
element = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Tic Tac Toe"]')
element.click()

# Steps 3:
# Click vào phần tử button "X":
element = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]')
element.click()

# Expect Result:
# Đóng màn hình Welcome và Xuất hiện màn hình GUI.

