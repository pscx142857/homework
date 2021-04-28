"""
将 login.txt 的文件 复制一份
"""
# 打开 源文件
fp = open("login.txt", "r", encoding="utf8")
# 创建 目标文件
new_fp = open("login-副本.txt", "w", encoding="utf8")

"""
# 将原文件 中的内容 读取出来
data = fp.read()  # 读取出来的是 字符串
# 将读取出来的数 写入 目标文件中
new_fp.write(data)
"""

# 将原文件 中的内容 读取出来
data = fp.readlines()  # 读取出来的是 列表
# 将读取出来的数 写入 目标文件中
new_fp.writelines(data)

# 关闭所有的文件
fp.close()
new_fp.close()
