__author__ = 'Administrator'
import time,unittest
from chandao.common.test_case_set import StartEnd

class TestAddBug(StartEnd):
   ''' add bugs suites '''

   def test_add_bug(self):
        '''用例说明：add bug'''
        title = "addbug" +  time.strftime("%Y-%m-%d_%H_%M_%S")
        self.bug.add_bug(title, "BODY")
        result = self.bug.is_add_bug_success(title)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()

