# 读取一个py文件，显示除了以井号(#)开头的行以外的所有行
"""
fp = open("作业文件.py", "r", encoding="utf8")  打开文件
data = fp.readlines()     按行读取所有内容保存在变量data中, 读取出的是列表, 每一行的内容就是列表中的元素
# print(data)
fp.close()                  关闭文件
for datas in data:          从列表中将内容变量出来保存在datas里
    if datas.startswith("#"):      如果datas里面的内容是是以#来头的行
        pass                      那么就过
    else:
        print(datas)           上面的条件都不满足就把datas打印出来
"""