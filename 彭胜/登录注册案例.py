"""
需求：
    1.程序启动，提示用户登录或者注册
    2.选择注册->要求输入用户名和密码->返回注册提示信息
    3.选择登录->要求输入用户和密码->判断是否登录成功
分析
    1.根据录入的1,2 判断用户为登录和注册
    2.注册: 将用户录入的用户名和密码以下面的格式写入到文件中
     用户名1|密码1
     用户名2|密码2
    3.登录: 读取出每一行并且通过|分割出来用户名和密码与用户录入的用户名和密码进行比对
"""
# 注册
def register():
    """
    根据用户输入的信息注册
    :return:
    """
    # 用户输入注册信息
    username = input("账号:")
    password = input("密码:")

    # 打开文件,以追加写的方式打开
    fp = open("user.txt","a",encoding="utf8")
    # 操作文件
    fp.write(f"{username}|{password}\n")
    print("恭喜你注册成功")
    # 关闭文件
    fp.close()
# 登录
def login():
    """
    根据用户输入的信息判断是否登录成功
    :return:
    """
    # 用户输入登录信息
    username = input("账号:")
    password = input("密码:")
    # 字符串拼接成txt文件里面保存的格式:用户名1|密码1
    user = f"{username}|{password}\n"

    # 打开文件
    fp = open("user.txt","r",encoding="utf8")
    # 操作文件,读取文件信息,得到的是一个列表
    ls = fp.readlines()
    # 遍历这个列表,得到每一行的信息
    for info in ls:
        # 和拼接的做对比,是否一样,一样则登录成功
        if info == user:
            print("恭喜你登录成功")
            # 登录成功后,结束循环
            break
    else:
        print("对不起,登录失败")
    # 关闭文件
    fp.close()
# 主程序
while True:
    st = input("请选择你需要的功能(1-注册 2-登录 3-退出):")
    # 根据用户输入选择功能
    if st == "1":
        # 调用注册函数
        register()
    elif st == "2":
        # 调用登录函数
        login()
    elif st == "3":
        exit("退出系统")
    else:
        print("对不起,请重新选择")