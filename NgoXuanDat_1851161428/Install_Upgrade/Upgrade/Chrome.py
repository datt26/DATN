# nhập thư viện appium
from appium import webdriver 

desired_cap = {
 	"uuid": "emulator-5554",
 	"platformName": "Android",
 	"platformVersion": "9", 
 	"appPackage": "com.ldmnq.launcher3",
 	"appActivity": "com.android.launcher3.Launcher",
 	"noReset": "true" 
 }

###
# TC: KIỂM TRA CẬP NHẬT GAME TRÊN TRÌNH DUYỆT:

# Steps 1:
# Kết nối vs thiết bị
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
# Cài đặt thời gian chờ phần tử xuất hiện
driver.implicitly_wait(30)

# Steps 2:
# Tìm phần tử trình duyệt Chrome trên giả lập
# Tiến hành vào Chrome 
element = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Chrome"]')
element.click()

# Steps 3:
# Tìm phần tử "Tìm kiếm"
# Điền từ khóa vào ô tìm kiếm
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText")
element.send_keys('tic tac toe wintrino')
driver.press_keycode(66) # gõ phím Enter

# Steps 4:
# Click vào kết quả tìm kiếm:
element = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.Image')
element.click()

# Steps 5:
# Click vào button "Cập nhật":
element = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button[2]')
element.click()

# Expect Result:
# Hiển thị và cho phép người chơi cập nhật game thông qua tìm kiếm trên trình duyệt.
# Dữ liệu game vẫn được lưu trữ.
