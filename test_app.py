import unittest
from app import add  # Import the add function from app.py

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Check if 2 + 3 equals 5
        self.assertEqual(add(-1, 1), 0)  # Check if -1 + 1 equals 0
        self.assertEqual(add(0, 0), 0)  # Check if 0 + 0 equals 0

if __name__ == "__main__":
    unittest.main()
