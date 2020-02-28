def input_password():

    # 1、提示用户输入密码
    password = input("请输入8位的密码：")

    # 2、判断密码长度 >=8，返回用户输入的密码
    if len(password) >= 8:
        return password

    # 3、如果小于 < 8 主动抛出异常
    print("主动抛出异常")
    # 1、创建异常对象  -可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够8位")

    # 2、主动抛出异常
    raise ex

# 捕获异常 -检测异常
try:
    print(input_password())

# 捕获异常 -处理异常
except Exception as result:
    print(result)
