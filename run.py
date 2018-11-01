# coding=utf-8


import unittest
from HTMLTestReportCN import HTMLTestRunner

if __name__ == '__main__':
    fp = open ('testReport.html', 'wb')
    loader = unittest.TestLoader ()
    suite = loader.discover (start_dir='./', pattern='*est.py')
    print(suite)
    runner = HTMLTestRunner (stream=fp, title='HTPP Inerface Test', description='This is report outout')
    runner.run (suite)
    fp.close ()
