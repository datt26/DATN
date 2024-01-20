# nhập thư viện appium
from appium import webdriver 

# Đầu đề mong muốn
desired_cap = {
 	"uuid": "emulator-5554", # id của thiết bị
 	"platformName": "Android",
 	"platformVersion": "9", 
 	#"app": "D:/@Documents/DO_AN_TOT_NGHIEP/SETUP/Tic Tac Toe_v8.0.60_apkpure.apk" # đường dẫn tới file apk
 	"appPackage": "com.ldmnq.launcher3", # tên gói dl của app
 	"appActivity": "com.android.launcher3.Launcher", # tên hoạt động của app
 	"noReset": "true" # giữ cho thiết bị không bị reset
 }

###
# TC: KIỂM TRA KẾT NỐI THIẾT BỊ VÀ VÀO GAME:

# Steps 1:
# Kết nối vs thiết bị
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
# Cài đặt thời gian chờ phần tử xuất hiện
driver.implicitly_wait(30)

# Steps 2:
# Tìm phần tử logo cài đặt game trên giả lập
# Tiến hành vào game 
element = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Tic Tac Toe"]')
element.click()

# Expect Result:
# Kết nối thiết bị và vào game thành công.
