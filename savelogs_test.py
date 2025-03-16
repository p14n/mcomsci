import unittest
import os
import tempfile
from io import StringIO
import sys
from savelogs import SaveLogs  # Assuming the SaveLogs function is in savelogs.py

class TestSaveLogs(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        # Capture stdout for testing print statements
        self.captured_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.captured_output
        
    def tearDown(self):
        # Clean up test files
        for filename in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, filename))
        os.rmdir(self.test_dir)
        # Reset stdout
        sys.stdout = self.original_stdout
        
    def test_save_logs_creates_file(self):
        # Test that SaveLogs creates a file if it doesn't exist
        test_filename = os.path.join(self.test_dir, "test_log.txt")
        test_data = "This is test log data"
        
        SaveLogs(test_data, test_filename)
        
        # Check if file was created
        self.assertTrue(os.path.exists(test_filename))
        
    def test_save_logs_writes_correct_data(self):
        # Test that SaveLogs writes the correct data to the file
        test_filename = os.path.join(self.test_dir, "test_log.txt")
        test_data = "This is test log data"
        
        SaveLogs(test_data, test_filename)
        
        # Read the file and check its contents
        with open(test_filename, 'r') as file:
            file_content = file.read()
        
        self.assertEqual(file_content, test_data)
        
    def test_save_logs_overwrites_existing_file(self):
        # Test that SaveLogs overwrites an existing file
        test_filename = os.path.join(self.test_dir, "test_log.txt")
        
        # Create file with initial content
        initial_data = "Initial data"
        with open(test_filename, 'w') as file:
            file.write(initial_data)
            
        # Now save new data using SaveLogs
        new_data = "New data"
        SaveLogs(new_data, test_filename)
        
        # Read the file and check its contents
        with open(test_filename, 'r') as file:
            file_content = file.read()
        
        # Verify the file contains only the new data
        self.assertEqual(file_content, new_data)
        
    def test_save_logs_handles_empty_string(self):
        # Test that SaveLogs can handle an empty string
        test_filename = os.path.join(self.test_dir, "test_log.txt")
        test_data = ""
        
        SaveLogs(test_data, test_filename)
        
        # Read the file and check its contents
        with open(test_filename, 'r') as file:
            file_content = file.read()
        
        self.assertEqual(file_content, test_data)
        
    def test_save_logs_success_message(self):
        # Test that SaveLogs prints a success message
        test_filename = os.path.join(self.test_dir, "test_log.txt")
        test_data = "This is test log data"
        
        SaveLogs(test_data, test_filename)
        
        # Check if success message was printed
        self.assertIn(f"Data successfully saved to {test_filename}", self.captured_output.getvalue())
        
    def test_save_logs_error_handling(self):
        # Test that SaveLogs handles errors properly
        # Using an invalid filename (a directory instead of a file)
        test_filename = self.test_dir  # This is a directory, not a file
        test_data = "This is test log data"
        
        SaveLogs(test_data, test_filename)
        
        # Check if error message was printed
        self.assertIn("Error saving data to", self.captured_output.getvalue())

if __name__ == '__main__':
    unittest.main() 