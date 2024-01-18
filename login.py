from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import unittest, csv, time

# thiết lập cài đặt của chrome để tắt thông báo khi test
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

"""
    4 test case
        - tc1 -> đăng nhập thành công với tài khoản đã được tạo, username/password đúng
        - tc2 -> đăng nhập thất bại với tài khoản đã được tạo, username đúng, passwword sai
        - tc3 -> đăng nhập thất bại với tài khoản đã được tạo, username sai, passwword đúng
        - tc4 -> đăng nhập thất bại với tài khoản chưa được đăng ký
    """


class TestFacebookLogin(unittest.TestCase):
    # hàm khởi tạo trình duyệt chrome dùng chung cho các test case
    def setUp(self):
        self.driver = webdriver.Chrome() # sử dụng Chrome
        self.driver.get("https://www.facebook.com/")
        time.sleep(5)

    # hàm tắt trình duyệt chrome khi kết thúc test case
    def tearDown(self):
        self.driver.quit()


    # tc1 -> đăng nhập thành công với tài khoản đã được tạo, username/password đúng
    def test_successful_login(self):
        try:
            # gọi phương thức đọc dữ liệu từ file .csv và truyền tham số
            data_list = self.read_csv("static/csv/tc1_successful_login.csv")
            for data in data_list:
                with self.subTest(data=data):
                    self.login(data['email'], data['password'])
                    # so sánh expected với page source của trang web -> True - in Test passed, False - in Test failed
                    self.assertTrue(data['expected'] in self.driver.page_source)
                    # in ra test passed nếu trả về True
                    print(f"\nTest Passed with email: {data['email'] } and password: {data['password']}" )
        except AssertionError:
            # in ra test failed nếu trả về false
            print(f"Test failed with email: {data['email'] } and password: {data['password']}")
            raise

    # tc2 -> đăng nhập thất bại với tài khoản đã được tạo, username đúng, passwword sai
    def test_failed_login_wrong_password(self):
        try:
            # gọi phương thức đọc dữ liệu từ file .csv và truyền tham số
            data_list = self.read_csv("static/csv/tc2_failed_login_wrong_password.csv")
            for data in data_list:
                with self.subTest(data=data):
                    self.login(data['email'], data['password'])
                    # so sánh expected với page source của trang web -> True - in Test passed, False - in Test failed
                    self.assertTrue(data['expected'] in self.driver.page_source)
                    print(f"\nTest Passed with email: {data['email']} and password: {data['password']}")
        except AssertionError as e:
            self.fail(f"Test case failed: {str(e)}")
            raise

    # tc3 -> đăng nhập thất bại với tài khoản đã được tạo, username sai, passwword đúng
    def test_failed_login_wrong_username(self):
        try:
            # gọi phương thức đọc dữ liệu từ file .csv và truyền tham số
            data_list = self.read_csv("static/csv/tc3_failed_login_wrong_username.csv")
            for data in data_list:
                with self.subTest(data=data):
                    self.login(data['email'], data['password'])
                    # so sánh expected với page source của trang web -> True - in Test passed, False - in Test failed
                    self.assertTrue(data['expected'] in self.driver.page_source)
                    # in ra test passed nếu trả về True
                    print(f"\nTest Passed with email: {data['email']} and password: {data['password']}")
        except AssertionError as e:
            # in ra test failed nếu trả về false
            self.fail(f"Test case failed: {str(e)}")
            raise

    # tc4 -> đăng nhập thất bại với tài khoản chưa được đăng ký
    def test_failed_login_not_register(self):
        try:
            # gọi phương thức đọc dữ liệu từ file .csv và truyền tham số
            data_list = self.read_csv("static/csv/tc4_failed_login_not_register.csv")
            for data in data_list:
                with self.subTest(data=data):
                    self.login(data['email'], data['password'])
                    # so sánh expected với page source của trang web -> True - in Test passed, False - in Test failed
                    self.assertTrue(data['expected'] in self.driver.page_source)
                    # in ra test passed nếu trả về True
                    print(f"\nTest Passed with email: {data['email']} and password: {data['password']}")
        except AssertionError as e:
            # in ra test failed nếu trả về false
            self.fail(f"Test case failed: {str(e)}")
            raise

    # phương thức đăng nhập
    def login(self, email, password):
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "pass").send_keys(password)
        self.driver.find_element(By.NAME, "login").click()
        time.sleep(10)

    # phương thức đọc dữ liệu từ file .csv
    def read_csv(self, file_path):
        data_list = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append(row)

        return data_list

    def test_login(self):
        try:
            # gọi phương thức đọc dữ liệu từ file .csv và truyền tham số
            data_list = self.read_csv("static/csv/login.csv")
            for data in data_list:
                with self.subTest(data=data):
                    self.login(data['email'], data['password'])
                    # so sánh expected với page source của trang web -> True - in Test passed, False - in Test failed
                    self.assertTrue(data['expected'] in self.driver.page_source)
                    # in ra test passed nếu trả về True
                    print(f"\nTest Passed with email: {data['email']} and password: {data['password']}")
        except AssertionError as e:
            # in ra test failed nếu trả về false
            self.fail(f"Test case failed: {str(e)}")
            raise


# chạy unitest
if __name__ == "__main__":
    unittest.main()