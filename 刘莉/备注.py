"""
#复制二进制文件-图片
sp = open("图片.png", "rb")         打开源文件
sp_new = open("图片-副本.png", "wb")     打开目标文件
data = sp.read()      将源文件的内容读出来
print(data)           将读出来的内容打印出来
sp_new.write(data)    将读出来的内容写在目标文件中
sp.close()           关闭源文件
sp_new.close()       关闭目标文件
# 复制大容量文件
fp = open(r"D\20210310软件测试精英班", "rb")    打开源文件
new_fp = open("副本.iso", "wb")       打开目标文件
data = fp.read(1024*1024)        读取第一份数据将读出来的内容保存在变量中,按照1024*1024的速度读取
while data:                    当data变量有数据的时候就继续循环执行 值到文件读完
    new_fp.write(data)          将读出来的内容写在新的目标文件
    data = fp.read(1024*1024)    继续读取下一份数据将源文件的内容读出来保存在变量里
fp.close()                        关闭源文件
new_fp.close()                   关闭目标文件
#复制文件
fp = open("barad.txt", "r", encoding="utf8")       #打开源文件
fp_new = open("barad副本.txt", "w", encoding="utf8")    #创建目标文件
# 操作文件
第一种方法
# data = fp.read()    将原文件中的内容读取出来 读取出来的是列表
# fp_new.write(data)      将读取出来的数写入目标文件中
第二种方法
data = fp.readlines()        将原文件中的内容读取出来 读取出来的是列表
fp_new.writelines(data)        将读取出来的数写入目标文件中
# 关闭文件
fp.close()     关闭文件fp
fp_new.close()   关闭文件fp_new
复制任意文件
第一种方法切片
fileName = input("请输入复制文件的路径:")     用变量保存需要复制文件的路径
num = fileName.rindex(".")               从右边第一个.获取索引号
newFileName = fileName[:num] + "-副本" + fileName[num:]       切片:语法:[开始:结束:步长]
fp = open(fileName, "r", encoding="utf8")             打开源文件
fp_new = open(newFileName, "w", encoding="utf8")      打开目标文件
data = fp.readlines()                           将原文件中的内容读取出来 读取出来的是列表
fp_new.writelines(data)              将读取出来的数写入目标文件中

第二种方法切割
li = fileName,rsplit(".",1)       使用.对文件进行切割,只切割一次
print(li)                           将切割后的文件打印出来
print(li[0]+"-副本."+li[1])             根据特定的形式进行打印

import os
os.rename("我喜欢的文件.png", "我喜欢的图片.png")    将文件我喜欢的文件重命名成我喜欢的图片
os.remove("草稿.txt")                删除文件草稿.txt
os.mkdir("草稿")    #创建目录

os.chdir("../")        改变执行目录为上一级目录
print(os.getcwd())       获取当前执行目录

print(os.listdir("../"))     获取目录列表下的所有内容
os.rmdir("草稿")              删除一个空目录
print(os.path.isfile("../python基础day07/password"))           判断password是不是一个文件
print(os.path.isdir("E:/python课堂练习笔记/python基础day07"))       判断day07是不是一个目录
name = os.path.splitext("barad.txt")               获取barad.txt的扩展名
print(name)
print(os.path.dirname(r"E:/python课堂练习笔记/python基础day07/复制图片.py"))    获取文件的路径
print(os.path.join(r"E:/python课堂练习笔记/python基础day07", "复制图片.py"))      将文件路径和文件名组装起来

def login():     打包函数
    username = input("请输入账号:")       请输入账号
    password = input("请输入密码:")           请输入密码
    login_info = f"{username},{password}\n"      设置变量保存账号密码
    fp = open("password", "a", encoding="utf8")    以追加的方式打开文件
    fp.write(login_info)              将用户录入的信息写入login_info中
    fp.close()                    关闭文件
    print("注册成功!")             提示
else:
    print("输入的序号不正确!")     如果输入的不是设定的序列号则提示不正确
def login1():                            打包以下函数
    username = input("请输入账号:")         请输入账号
    password = input("请输入密码:")        请输入密码
    fp = open("password","r",encoding="utf8")   以只读的方式打开文件
    data = fp.readlines()                   按行读取所有内容保存在变量data中, 读取出的是列表, 每一行的内容就是列表中的元素
    fp.close()                            关闭文件
    for i in data:                           从data中遍历数据然后保存在i里面
        string = f"{username},{password}\n"    设置变量保存账号密码
        if string == i:                 如果用户输入的数据等于从文件中保存是账号密码
            print("登录成功!")          那么登录成功
            break                     否则终止循环
    else:
        print("用户名或者密码错误!")     如果上面的条件都不满足,那么提示错误
        第二种方法
    for i in data:                   从data中遍历数据然后保存在i里面
        string = i.replace("\n", "")       将i中的数据\n替换为空并且保存在变量string中
        li = string.split(",")             将变量中保存的数据通过,进行分割,分割以后保存在变量li中
        if li[0] == username and li[1] == password:           用户输入的数据和文件保存的数据相等
            print("登录成功")         那么登录成功
            break        否则终止循环
    else:
        print("用户名或者密码错误!")         如果上面的条件都不满足,那么提示错误
while 1:                                  当循环条件为真
    num = input("提示信息(1-选择注册 2-登录):")       请按要求输入提示信息
    if num == "1":                        如果输入1
        login()                         那么就调用login函数
    elif num == "2":                      如果输入2
        login1()                         那么就调用login1()函数
"""
