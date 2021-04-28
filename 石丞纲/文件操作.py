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

while True:
    num = input("请输入序号选择操作的功能(1-登录, 2-注册)")  # 定义num

   # 定义函数名
    def dl():
      # 输入用户名
        username = input("请输入用户名:")
          # 输入密码
        password = input("请输入密码:")
           # 打开文件
        fp = open("test.txt", "r", encoding="utf8")
          # 打开文件的方式
        data = fp.readlines()
           # 关闭文件
        fp.close()
          # 打印
        print(data)
          # 遍历
        for i in data:
            # 操作文件
            string = f"{username}, {password}\n"
            # 判断
            if string == i:
                # 打印
                print("登录成功")
                # 退出循环
                break
        else:   
            print("用户名或者密码错误")


    # 输入数字进行操作
    if num == "1":
        # 调用
        dl()
        # 输入数字进行操作
    elif num == "2":
        # 遍历
        def zc():
            # 输入姓名
            username = input("请输入用户名:")
            # 输入姓名
            password = input("请输入密码:")
            # 打开文件
            fp = open("test.txt", "a", encoding="utf8")
            # 操作文件
            fp.write(f"{username}, {password}\n")
            # 关闭文件
            fp.close()
            print("注册成功")
        # 遍历
        zc() 


# 打开源文件
# fp = open("test.txt", "r", encoding="utf8")
# 创建目标文件
# new_fp = open("text-副本.txt", "w", encoding="utf8")
# 读取源文件
# data = fp.read()
# 写入目标文件中
# new_fp.write(data)
# 关闭
# fp.close()
# new_fp.close()

# 输入路径
# fileName = input("请输入复制文件路径:")
# 从左往右分割
# num = fileName.rindex(".")
# 链接
# newFileName = fileName[:num] + "-副本" + fileName[num:]
# 打印
# print(newFileName)

# # 打开源文件
# fp = open("newFileName", "r", encoding="utf8")
# # 创建目标文件
# new_fp = open("newFileName", "w", encoding="utf8")
# # 读取源文件
# data = fp.read()
# # 写入目标文件中
# new_fp.write(data)
# # 关闭
# fp.close()
# new_fp.close()


# # 打开源文件
# fp = open("15_文件的操作语法.mp4", "rb")
# # 打开创建的文件
# new_fp = open("15_文件的操作语法-副本.mp4", "wb")
# # 读取源文件
# date = fp.read()
# print(date)
# # 将源文件写入目标文件
# new_fp.write(date)
# # 关闭
# fp.close()
# new_fp.close()

import os

# 文件重命名
# os.rename("test.txt", "test1.txt")

# 删除文件
# os.remove("text-副本.txt")

# 创建文件夹
# os.mkdir("D:\python 代码\code\\28")

# 获取当前执行目录
# print(os.getcwd())

# 改变执行目录
# os.chdir("D:\python 代码\code\\27")

# 获取目录列表
# li = os.listdir("D:\python 代码\code\\27")
# print(os.listdir)

# 删除目录
# os.rmdir("D:\python 代码\code\代码28")

import os
# 判断是否为目录(文件夹)或者是文件
# print(os.path.isdir("D:\python 代码\code\27"))
# print(os.path.isfile("D:\python 代码\code\27"))

# 获取文件扩展名
# print(os.path.splitext("文件操作.py"))

# 获取文件路径
# print(os.path.splitext(""))

# 组装文件路径
# print(os.path.join(r"D:\pyth    on 代码\code\21", "test1.txt"))
