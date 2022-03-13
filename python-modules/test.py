"""Unit Testing."""
import unittest
import guess_number


class TestGuessNumber(unittest.TestCase):
    """Object class for unit testing."""

    def setUp(self):
        """Information function."""
        print("\nStarting unit test for guess_number module")

    def test_guess_01(self):
        """Test Case 01."""
        test_start = 1
        test_end = 3
        result = guess_number.guess_game(test_start, test_end)
        self.assertEqual(result, "You guessed it right")

    def test_guess_02(self):
        """Test Case 02."""
        test_start = 5
        test_end = 3
        result = guess_number.guess_game(test_start, test_end)
        self.assertIsInstance(result, ValueError)

    def tearDown(self) -> None:
        """End of test."""
        print("Test completed")


if __name__ == '__main__':
    unittest.main()
