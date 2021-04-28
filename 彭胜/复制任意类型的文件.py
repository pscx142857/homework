"""
    可以复制任意类型的文件,使用二进制的方式读写
"""
# 打开文件
fp = open("图片.ico","rb")
new_fp = open("图片-副本.ico","wb")
# 操作文件
data = fp.read()
new_fp.write(data)
# 关闭文件
fp.close()
new_fp.close()