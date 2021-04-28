"""
    将test.py复制一份,文件名为test-副本.py
"""
# 打开文件
fp = open("test.py","r",encoding="utf8")
new_fp = open("test-副本.py","w",encoding="utf8")
# 操作文件
# 读取原文件里面的所有信息
data = fp.read()
# 将读取到的信息写入目标文件
new_fp.write(data)
# 关闭文件
fp.close()
new_fp.close()