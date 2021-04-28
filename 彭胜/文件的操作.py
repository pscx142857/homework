import os
# .1.文件重命名
# 语法:
# os.rename("旧文件路径", "新的文件路径")
# os.rename("test-副本.py","ps.py")
# .2.删除文件
# 语法:
# os.remove("文件路径")
# os.remove("删除我.txt")
# .3.创建文件夹
# 语法:
# os.mkdir("文件夹路径")
# os.mkdir("创建一个文件夹")
# .4.获取当前执行目录（就是点击run的py文件所在目录）
# 语法:
# os.getcwd()
# print(os.getcwd()) # C:\Users\Administrator\PycharmProjects\Python基础\作业\Python基础第七天
# .5.改变执行目录
# 通常情况下，我们的执行目录就是点击run的py文件所在的目录，但是我们也可以改变执行目录
# 语法:
# os.chdir(“目录路径”)
# os.chdir(r"C:\Users\Administrator\PycharmProjects\Python基础\作业\Python基础第六天")
# print(os.getcwd())
# .6.获取目录列表
# 语法:
# 列表变量 = os.listdir("目录路径")
# print(os.listdir("../Python基础第七天"))
# .7.删除目录
# 语法:
# os.rmdir("目录路径")
# 注意：只能够删除一个空目录
# 如果需要删除非空的目录需要用到其他的模块，这我们之后在讲。
# os.rmdir("创建一个文件夹")
# .8.判断是否为目录(文件夹)
# 或者是文件
# 语法:
# os.path.isdir("目录路径")
# 判断该文件是否为一个目录(文件夹)
# os.path.isfile("文件路径")
# 判断路径是否为一个文件
# 注意以上写法有path的哦
# print(os.path.isdir("../Python基础第七天")) # True
# print(os.path.isfile("test.py")) # True
# .9.获取文件扩展名
# 语法:
# os.path.splitext("文件名")
# 注意以上写法有path的哦
# print(os.path.splitext("ps.py"))
# .10.获取文件路径
# 语法:
# os.path.dirname("文件名")
# 注意以上写法有path的哦
# print(os.path.dirname("ps.py"))
# .11.组装文件路径
# 语法:
# os.path.join("目录路径", "文件名")
# 注意以上写法有path的哦
print(os.path.join("../", "ps.py"))