import unittest
import Capfile
class Cap_test_cases(unittest.TestCase):
    def test_one_letter(self):
        text="python"
        result=Capfile.Cap(text)
        self.assertEqual(result,"Python")
    def  test_sentence(self):
        self.assertEqual(Capfile.Cap("python rocks"),"Python Rocks")
if __name__=="__main__":
    unittest.main()
        