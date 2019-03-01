import unittest
import HTMLTestRunner
import os
from testsuite.test_forum import FomerSearch
from testsuite.test_delete import DeleteTest
from testsuite.test_search import SearchTest
from testsuite.test_vote import VoteTest

cur_path=os.path.dirname(os.path.abspath("."))
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path):os.mkdir(report_path)

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(FomerSearch))
suite.addTest(unittest.makeSuite(DeleteTest))
suite.addTest(unittest.makeSuite(SearchTest))
suite.addTest(unittest.makeSuite(VoteTest))

if __name__=="__main__":
    html_report=report_path+r'/result.html'
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="论坛测试报告",description="用例执行情况")
    runner.run(suite)