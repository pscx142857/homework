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
"""
# 1.注册登录案例
"""
# 1.程序启动，提示用户登录或者注册
#   根据录入的1,2 判断用户为登录和注册
while True:
    num = input("请输入序号,选择需要操作的功能(1-注册 2-登录 3-退出):")  # 输入的是 字符串
    if num == "1":
        print("******* 请注册 *******")
        # 2.选择注册->要求输入用户名和密码->返回注册提示信息
            # 注册: 将用户录入的用户名和密码以下面的格式 写入到文件中
            # 用户名1|密码1
            # 用户名2|密码2
        username = input("请输入用户名:")
        password = input("请输入密码:")
        info = f"{username}|{password}\n"   # info 是 字符串
        # print(info)  # betty|123456
        # 打开文件
        fp = open("login.txt", "a", encoding="utf8")
        # 操作文件 写入内容
        fp.write(info)
        # 关闭文件
        fp.close()
        print("*注册成功!!*")

    elif num == "2":
        # 3.选择登录->要求输入用户和密码->判断是否登录成功
        #   登录: 读取出每一行 并且通过 | 分割出来 用户名和密码与用户录入的用户名和密码进行比对
        print("******* 请登录 *******")
        username = input("请输入用户名:")
        password = input("请输入密码:")
        # 将客户输入的用户名和密码 组装成  betty|123456
        user_info = f"{username}|{password}\n"
        # print(user_info)   # betty|123456
        # 以读的方式 打开文件
        fp = open("login.txt", "r", encoding="utf8")
        # 读取文件中的所有的 用户名和密码  -->读出来是 列表
        data = fp.readlines()    # ['betty|123456\n', 'mary|123456\n', 'joke|123456\n']
        fp.close()

        # 方法一:
        # for i in data:
        #     if user_info == i:
        #         print("*登录成功!!*")
        #         break  # 找到了就不找了
        # else:
        #     print("用户名或者密码有误,登录失败!")

        # 方法二:
        for i in data:  # i = 'betty|123456\n'
            # 先去掉\n
            new_i = i.replace("\n", "")  # 'betty|123456'
            N_i = new_i.split("|")  # ['betty', '123456']  --> 分隔出来是列表
            if N_i[0] == username and N_i[1] == password:
                print("登陆成功!!")
                break  # 找到了就不找了
        else:
            print("用户名或者密码有误,登录失败!")

    elif num == "3":
        exit("退出系统!!")


"""
2.文本的复制:
    将 将 test.txt 的文件 复制一份
"""
# 以读的方式 打开 test.txt
fp = open("test.txt", "r", encoding="utf8")
# 读取文件 所有内容
# data = fp.read()   # --->读取出来的内容是 字符串
data = fp.readlines() #  --->读取出来的是 列表
# 关闭文件
fp.close()

# 创建(打开)目标文件 test-副本.txt
new_fp = open("test-副本.txt", "w", encoding="utf8")
# 写入读取的 data 到目标文件
# new_fp.write(data)  # -->写入的是 字符串
new_fp.writelines(data)  # --> 写入的是 列表
# 关闭 目标文件
new_fp.close()

"""
3.复制任意 文本文件
"""
fileName = input("请输入需要复制文件的路径:")  # 01回顾文件操作.py
# 得到新的文件路径?  -->得到 新文件名的方法
li = fileName.rsplit(".", 1)
print(li)  # ['01回顾文件操作', 'py']
newFileName = li[0] + "-副本." + li[1]

# 打开 源文件
fp = open(fileName, "r", encoding="utf8")
# 创建 目标文件
new_fp = open(newFileName, "w", encoding="utf8")  # 01回顾文件操作-副本.py

# 将原文件 中的内容 读取出来
data = fp.readlines()  # 读取出来的是 列表
# 将读取出来的数据 写入 目标文件中
new_fp.writelines(data)

# 关闭所有的文件
fp.close()
new_fp.close()


"""
4.任意类型文件 复制
    复制 图片 : 图片.jpeg
"""
# 打开源文件
fp = open("图片.jpeg", "rb")
# 打开目标文件
new_fp = open("图片-副本.jpeg", "ab")

# 读取源文件内容
data = fp.read()
# 将读取的内容写入目标文件
new_fp.write(data)

# 关闭所有文件
fp.close()
new_fp.close()

""""
5.复制大文件
"""
# 打开源文件
fp = open(r"D:\20210310软件测试精英班\03.Linux操作系统\2021-3-24-Linux基础操作-day01\resource\CentOS-7-x86_64-DVD-2003.iso", "rb")
# 打开目标文件
new_fp = open("CentOS-7-x86_64.iso", "wb")

# 将源文件的内容读取出来
data = fp.read(1024 * 1024)  # 先读取 第一份数据
while data:  # 当data 中有数据时
    # 将读取的数据写入目标文件
    new_fp.write(data)  # 写入
    data = fp.read(1024 * 1024)  # 读取下一份数据

# 关闭所有的文件
fp.close()
new_fp.close()


import shutil

# 文件的复制
# shutil.copyfile("源文件", "复制粘贴后新的文件名")
shutil.copyfile("图片-副本.jpeg", "图片-本.jpeg")


# 非空目录的删除
# shutil.rmtree("目录名")
shutil.rmtree("shanc")


