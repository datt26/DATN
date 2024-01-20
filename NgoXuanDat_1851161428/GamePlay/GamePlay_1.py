
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
# TC: KIỂM TRA GAMEPLAY CỦA CHẾ ĐỘ CHƠI ĐƠN:

# Steps 1:
# Kết nối thành công
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Steps 2:
# Tiến hành vào game 

# Steps 3:
# Đóng màn hình Welcome

# Steps 4:
# Click vào khu vực chơi game.
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View[2]")
element.click()
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View[4]")
element.click()
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View[6]")
element.click()
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[3]/android.view.View[2]")
element.click()
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[3]/android.view.View[4]")
element.click()
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[3]/android.view.View[6]")
element.click()
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[5]/android.view.View[2]")
element.click()
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[5]/android.view.View[4]")
element.click()
element = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[5]/android.view.View[6]")
element.click()

# Expect Result:
# Trò chơi sẽ thắng khi 3 quân cờ "X" hoặc "O" nằm trên cùng 1 hàng.
# Trò chơi sẽ hòa khi tất cả các vị trí trên bàn cờ đã được đánh nhưng vẫn không thỏa mãn điều kiện thắng.
# Ngay sau khi người chơi đánh sẽ đến lượt của máy đánh ở 1 vị trí ngẫu nhiên trên bàn cờ.
# Lượt đi đầu của ván đấu tiếp theo sẽ là lượt của người thắng ván đấu trước.
# Khi hòa lượt đi đầu của ván đấu tiếp theo sẽ thay đổi lần lượt giữa "X" và "O".
