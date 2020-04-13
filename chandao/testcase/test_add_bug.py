__author__ = 'Administrator'
import time,unittest
from chandao.common.test_case_set import StartEnd

class TestAddBug(StartEnd):

   def test_add_bug(self):
        title = "addbug" +  time.strftime("%Y-%m-%d_%H_%M_%S")
        self.bug.add_bug(title, "BODY")
        result = self.bug.is_add_bug_success(title)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()

