import unittest
import lib


class TestLibFunctions(unittest.TestCase):
    # Test if data loading function returns expected output format
    def test_load_data(self):
        data = lib.load_data('data.csv')
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIsInstance(data[0], dict)


    # This is a mock test for demonstration. Replace it with your actual testing logic.
    def test_display_dataset_head(self):
        result = lib.display_dataset_head(lib.load_data('data.csv'))
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
