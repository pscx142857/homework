# 1. 上课案例 实现一遍
# 2. 读取一个py文件，显示除了以井号(#)开头的行以外的所有行
# 3. 预习 面向对象

# 打开文件
fp = open("文件操作.py", "r", encoding="utf8")
# 读取文件
date = fp.readlines()
print(date)
# 显示除#号开头的所有行
for i in date:
    if i.startswith("#"):
        pass
    else:
        print(i)

