import unittest
from unittest.mock import patch
import io
import sys
from addition_game import play_addition_game  # Assuming the previous code is saved in addition_game.py

class TestAdditionGame(unittest.TestCase):
    
    @patch('random.randint')
    @patch('builtins.input')
    def test_all_correct_answers(self, mock_input, mock_randint):
        # Set up the random numbers to be returned
        mock_randint.side_effect = [5, 7, 3, 8, 2, 4]  # Will return these values in sequence
        
        # Set up the user inputs
        mock_input.side_effect = ["12", "11", "6"]  # Correct answers for the questions
        
        # Capture stdout to check output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Run the game
        play_addition_game()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check if the final score is 3
        self.assertIn("Your final score is: 3 out of 3", captured_output.getvalue())
    
    @patch('random.randint')
    @patch('builtins.input')
    def test_some_incorrect_answers(self, mock_input, mock_randint):
        # Set up the random numbers to be returned
        mock_randint.side_effect = [5, 7, 3, 8, 2, 4]
        
        # Set up the user inputs (first one wrong, others correct)
        mock_input.side_effect = ["10", "11", "6"]
        
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Run the game
        play_addition_game()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check if the final score is 2
        self.assertIn("Your final score is: 2 out of 3", captured_output.getvalue())
    
    @patch('random.randint')
    @patch('builtins.input')
    def test_invalid_input(self, mock_input, mock_randint):
        # Set up the random numbers
        mock_randint.side_effect = [5, 7, 3, 8, 2, 4]
        
        # Set up user inputs (one invalid, others correct)
        mock_input.side_effect = ["abc", "11", "6"]
        
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Run the game
        play_addition_game()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check if invalid input was handled and final score is 2
        self.assertIn("That's not a valid number", captured_output.getvalue())
        self.assertIn("Your final score is: 2 out of 3", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
