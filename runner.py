import unittest
from test import Test001
import HTMLTestRunner


suite = unittest.TestLoader().loadTestsFromTestCase(Test001)


fp = file('my_report.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='My test',
    description='IPv6 test'
)

runner.run(suite)