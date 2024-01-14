import unittest, os
from HtmlTestRunner import HTMLTestRunner

from login import TestFacebookLogin
from avatar import TestFacebookAvatar

# get dir path to output report file
dir = os.getcwd()

# get all tests from login and avatar tests
login = unittest.TestLoader().loadTestsFromTestCase(TestFacebookLogin)
change_avatar = unittest.TestLoader().loadTestsFromTestCase(TestFacebookAvatar)

# create a test suite combing two test classs
test_suite = unittest.TestSuite([login, change_avatar])

# open report file
outfile = open(dir + "\SeleniumReport.html", "w")

# set htmltestrunner config options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report',description='Acceptance Tests')

# Run the test suite using htmTestRunner
runner.run(test_suite)