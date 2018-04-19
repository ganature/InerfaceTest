import os
import copy
e=[]
a=['a','b',e]
b=copy.copy(a)
c=copy.deepcopy(a)
b[2]='aaa'
# print a
# print id(a),id(a[0])
# print b
# print id(b),id(b[0])
# print os.getcwd ()
# print os.listdir ('E:\GitHub\InerfaceTest')