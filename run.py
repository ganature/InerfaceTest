# coding=utf-8


import unittest
import HTMLTestRunner

if __name__ == '__main__':
    fp=open ('testReport.html', 'w')
    loader=unittest.TestLoader ()
    suite=loader.discover (start_dir='./', pattern='*est.py')
    runner=HTMLTestRunner.HTMLTestRunner (stream=fp, title='HTPP Inerface Test', description='This is report outout')
    runner.run (suite)
    fp.close()