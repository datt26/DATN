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
# TC: KIỂM TRA CHECKBOX "DON'T SHOW AGAIN" Ở GIAO DIỆN WELCOME (SAU):

# Steps 1:
# Kết nối thành công
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Steps 2:
# Tiến hành vào game:
element = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Tic Tac Toe"]')
element.click()

# Steps 3:
# Tìm phần tử checkbox "Don"t show again" và click:
element = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View/android.view.View[7]/android.widget.Image')
element.click()

# Expect Result:
# Khi tick vào checkbox "Don't show again" <=> Bỏ tick checkbox "Welcome screen" ở giao diện Setting.
# Checkbox "Welcome screen" ở giao diện Setting được bỏ tick. (Kiểm tra TC Setting ở mục GUI)
# Màn hình Welcome không xuất hiện khi vào game. (Kiểm tra TC Start)

