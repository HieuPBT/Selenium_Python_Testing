from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
import unittest, csv, time

"""
    4 test case
        - tc1 -> kích thước <= 4MB, đúng định dạng ảnh - Thay đổi ảnh thành công
        - tc2 -> kích thước <= 4MB, sai định dạng ảnh - Báo lỗi Can't read files
        - tc3 -> kích thước > 4MB, đúng định dạng ảnh - Báo lỗi Can't read files
        - tc4 -> kích thước > 4MB, sai định dạng ảnh - Báo lỗi Can't read files
        
    """
# thiết lập cài đặt của chrome để tắt thông báo khi test
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")


class TestFacebookAvatar(unittest.TestCase):
    # hàm khởi tạo trình duyệt chrome dùng chung cho các test case
    def setUp(self):
        self.driver = webdriver.Chrome(options=chrome_options)  # sử dụng Chrome
        self.driver.get("https://www.facebook.com/")
        time.sleep(5)
        self.login('0869309402', 'Qwerty123@')
        time.sleep(5)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a/div[1]/div[2]/div/div/div/div/span/span").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[text()='Edit profile']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/span/div/div[2]/div/div[2]/div/div/span/span").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[text()='Upload Photo']").click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

    # tc1 -> kích thước <= 4MB, đúng định dạng ảnh - Thay đổi ảnh thành công
    def test_successful_change_avatar(self):
        try:
            # gọi phương thức đọc dữ liệu từ file .csv và truyền tham số
            data_list = self.read_csv("static/csv/tc1_successfull_change_avatar.csv")
            for data in data_list:
                with self.subTest(data=data):
                    # hàm truyền đường dẫn file ảnh
                    keyboard = Controller()
                    keyboard.type(data[r'file_path'])
                    keyboard.press(Key.enter)
                    time.sleep(5) # chờ website load
                    # so sánh expected với page source của trang web -> True - in Test passed, False - in Test failed
                    self.assertTrue(data['expected'] in self.driver.page_source)
                    # in ra test passed nếu trả về True
                    print(f"\nTest Passed with image: {data[r'file_path']}")
        except AssertionError as e:
            # in ra test failed nếu trả về false
            print(f"Test failed with image: {data[r'file_path']}")
            raise

    # tc2 -> kích thước <= 4MB, sai định dạng ảnh - Báo lỗi Can't read files
    def test_failed_change_avatar_wrong_format(self):
        try:
            # gọi phương thức đọc dữ liệu từ file .csv và truyền tham số
            data_list = self.read_csv("static/csv/tc2_failed_change_avatar_wrong_format.csv")
            for data in data_list:
                with self.subTest(data=data):
                    # hàm truyền đường dẫn file ảnh
                    keyboard = Controller()
                    keyboard.type(data[r'file_path'])
                    keyboard.press(Key.enter)
                    time.sleep(5)
                    # so sánh expected với page source của trang web -> True - in Test passed, False - in Test failed
                    self.assertTrue(data['expected'] in self.driver.page_source)
                    # in ra test passed nếu trả về True
                    print(f"\nTest Passed with image: {data[r'file_path']}")
        except AssertionError as e:
            # in ra test failed nếu trả về false
            self.fail(f"Test failed: {str(e)}")
            raise

    # tc3 -> kích thước > 4MB, đúng định dạng ảnh - Báo lỗi Can't read files
    def test_failed_change_avatar_wrong_size(self):
        try:
            # gọi phương thức đọc dữ liệu từ file .csv và truyền tham số
            data_list = self.read_csv("static/csv/tc3_failed_change_avatar_wrong_size.csv")
            for data in data_list:
                with self.subTest(data=data):
                    # hàm truyền đường dẫn file ảnh
                    keyboard = Controller()
                    keyboard.type(data[r'file_path'])
                    keyboard.press(Key.enter)
                    time.sleep(5)
                    # so sánh expected với page source của trang web -> True - in Test passed, False - in Test failed
                    self.assertTrue(data['expected'] in self.driver.page_source)
                    # in ra test passed nếu trả về True
                    print(f"\nTest Passed with image: {data[r'file_path']}")
        except AssertionError as e:
            # in ra test failed nếu trả về false
            self.fail(f"Test failed: {str(e)}")
            raise

    # tc4 -> kích thước > 4MB, sai định dạng ảnh - Báo lỗi Can't read files
    def test_failed_change_avatar(self):
        try:
            # gọi phương thức đọc dữ liệu từ file .csv và truyền tham số
            data_list = self.read_csv("static/csv/tc4_failed_change_avatar.csv")
            for data in data_list:
                with self.subTest(data=data):
                    # hàm truyền đường dẫn file ảnh
                    keyboard = Controller()
                    keyboard.type(data[r'file_path'])
                    keyboard.press(Key.enter)
                    time.sleep(10)
                    # so sánh expected với page source của trang web -> True - in Test passed, False - in Test failed
                    self.assertTrue(data['expected'] in self.driver.page_source)
                    # in ra test passed nếu trả về True
                    print(f"\nTest Passed with image: {data[r'file_path']}")
        except AssertionError as e:
            # in ra test failed nếu trả về false
            self.fail(f"Test failed: {str(e)}")
            raise

    # phương thức đăng nhập
    def login(self, email, password):
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "pass").send_keys(password)
        self.driver.find_element(By.NAME, "login").click()
        time.sleep(3)

    # phương thức đọc dữ liệu từ file .csv
    def read_csv(self, file_path):
        image_list = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                image_list.append(row)

        return image_list



if __name__ == "__main__":
    unittest.main()