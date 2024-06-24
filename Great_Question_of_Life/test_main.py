import unittest
from main import check_answer

class TestGreatQuestionOfLife(unittest.TestCase):

    def test_check_answer(self):
        # Test cases for different valid inputs\
        correct_ans="Yes, 42 is indeed the answer to the ultimate question of life, the universe, and everything!"
        incorect_ans="Incorect answer human"
        self.assertEqual(check_answer("42"), correct_ans)  
        self.assertEqual(check_answer("forty-two"), correct_ans)
        self.assertEqual(check_answer("forty two"), correct_ans)
        self.assertEqual(check_answer("Forty-Two"), correct_ans)  # case sensitive test
        self.assertEqual(check_answer("  forty two  "), correct_ans) # negative and positive space check
        
        # Test cases for invalid inputs
        self.assertEqual(check_answer("43"),incorect_ans)
        self.assertEqual(check_answer("forty three"), incorect_ans)
        self.assertEqual(check_answer("Hello World"), incorect_ans)

if __name__ == '__main__':
    unittest.main()
