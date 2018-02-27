# coding=utf-8

# 数据库信息
MySQL_HOST='120.77.216.30'
MySQL_USER='root'
MySQL_PASSWORD='womendeceshihahahah7788'
MySQL_DB='ppt_schema'
# 管理员登录接口
LOGIN_INERFACE_BASEURL = 'http://www.tietonggroup.com/ttsd/publicNumber/login?key='
LOGIN_SYSUSER_PARM = {"userName": "linzj", "password": "123"}

# 创建三级管理员接口
SYSUSER_CREAT_INERFACE = 'http://www.tietonggroup.com/ttsd/api/publicNumber/sysUser/create?' \
                       'token=%(token)s&sign=%(sign)s&loginName=%(loginName)s&password=%(password)s&name=%(name)s'
SYSUSER_CREAT_INERFACE_PARM = ['token', 'loginName', 'password', 'name']
"""
参数定义
    序号	     参数	    类型	        必填	         说明
    1       loginName   String      是            用户账号，支持中文、英文、数字和下划线
    2	    name	    String	    否	          用户名称，不少于3位字符
    3	    password	String	    是	          用户密码，不少于3位字符
返回结果
执行http请求后返回结果参数为：
    序号	    名称	        类型	        说明
    1	    status	    int	        返回码
    2	    message	    String	    返回说明
    3	    total	    int	        返回数据数量
返回结果为JSON数据格式：
{"status":1000,"message":"ok","total":0}

"""

# 修改管理员接口
SYSUSER_EDIT_INERFACE='http://www.tietonggroup.com/sd/api/publicNumber/sysUser/edit?token=%(token)s&sign=%(sign)s' \
                      '&loginName=%(loginName)s&name=%(name)s&password=%(password)s'
SYSUSER_EDIT_INERFACE_PARM=['token', 'loginName', 'password', 'name']
"""
参数定义
    序号	     参数	    类型	        必填	         说明
    1       loginName   String      是            用户账号，支持中文、英文、数字和下划线
    2	    name	    String	    否	          用户名称，不少于3位字符
    3	    password	String	    否	          用户密码，不少于3位字符
"""


# 新增群组接口
GROUP_ADD_INERFACE='http://www.tietonggroup.com/sd/api/publicNumber/group/create?'

# 修改群组接口
GROUP_EDIT_INERFACE='http://www.tietonggroup.com/sd/api/publicNumber/group/edit?'

# 查询群组接口
GROUP_LIST_INERFACE='http://www.tietonggroup.com/sd/api/publicNumber/group/list?'

# 删除群组接口
GROUP_DELETE_INERFACE='http://www.tietonggroup.com/sd/api/publicNumber/group/delete?'


# 新增用户接口
PTTUSER_ADD_INERFACE='http://www.tietonggroup.com/sd/api/publicNumber/pttUser/create?'

# 修改用户接口
PTTUSER_EDIT_INERFACE='http://www.tietonggroup.com/sd/api/publicNumber/pttUser/edit?'

# 查询用户接口
PTTUSER_LIST_INERFACE='http://www.tietonggroup.com/sd/api/publicNumber/pttUser/list?'

# 删除用户接口
PTTUSER_DELETE_INERFACE='http://www.tietonggroup.com/sd/api/publicNumber/pttUser/delete?'