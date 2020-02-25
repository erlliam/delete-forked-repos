import unittest
import config

class TestConfig(unittest.TestCase):
    
    def test_url(self):
        self.assertEqual(config.url.lower(), "https://api.github.com")

class TestMain(unittest.TestCase):

if __name__ == '__main__':
    unittest.main()
