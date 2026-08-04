from code2test.Extra3 import read_lines
import unittest
from unittest.mock import patch, mock_open

class TestFileRead(unittest.TestCase):
    #Arrange
    @patch('builtins.open', new_callable=mock_open, read_data="Read this text")
    def test_read_config(self, mockfile):
        #Act
        result = read_lines("path.txt")
        #Assert
        self.assertEqual(result, ["Read this text"])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_file_not_found(self, mockfile):
        #Act & Assert
        with self.assertRaises(FileNotFoundError):
            read_lines('path.txt')

if __name__ == '__main__':
    unittest.main()