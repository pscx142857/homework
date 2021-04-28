# 2. 读取一个py文件，显示除了以井号(#)开头的行以外的所有行
# 打开文件
fp = open("test.py","r",encoding="utf8")
# 操作文件
# 按行读取,得到一个列表
data = fp.readlines()
# 遍历这个列表
for i in data:
    # 依次判断里面的元素是否以#开头的
    if i.startswith("#"):
        pass
    # 显示除了以#号开头的以外的所有行
    else:
        print(i)
# print(data)
# 关闭文件
fp.close()