import unittest
from login import TestFacebookLogin
from avatar import TestFacebookAvatar

# get all test from class tesstfacebook login và testfacebookavatar
login = unittest.TestLoader().loadTestsFromTestCase(TestFacebookLogin)
change_avatar = unittest.TestLoader().loadTestsFromTestCase(TestFacebookAvatar)

# create a test suite combing two test classs
test_suite = unittest.TestSuite([login, change_avatar])

# run the suite
unittest.TextTestRunner(verbosity=3).run(test_suite)