"""
define a valid email address with regex

assertTrue
assertFalse

"""

import unittest
import re

def email_validator(email):
    if len(email) > 7:
        if re.match(r'^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$', email) != None:
            return True
    return False

class TestEmailValidator(unittest.TestCase):

    def test_email_validator_valid(self):
        self.assertTrue(email_validator('test@example.com'))
        self.assertTrue(email_validator('test+123@example.com'))
        self.assertTrue(email_validator('test_123@example.co.uk'))

    def test_email_validator_invalid(self):
        self.assertFalse(email_validator('test'))
        self.assertFalse(email_validator('test@'))
        self.assertFalse(email_validator('test@example'))
        self.assertFalse(email_validator('test@example.'))

    def test_email_validator_regex(self):
        valid_email = 'example123@test.com'
        invalid_email = 'example@testcom'

        regex_pattern = r'^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$'

        self.assertTrue(re.match(regex_pattern, valid_email))
        self.assertFalse(re.match(regex_pattern, invalid_email))

if __name__ == '__main__':
    unittest.main()