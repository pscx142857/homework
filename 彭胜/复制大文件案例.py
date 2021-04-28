"""
 文件太大,全部二进制读取会内存溢出,这个时候需要边读边写
 读一部分,写一部分,再去读一部分
 知道读出来的数据为空时,不再进行读写
"""
# 打开文件
fp = open("test.py","rb")
new_fp = open("test-副本.py","wb")
# 操作文件
data = fp.read(2)
while data:
    new_fp.write(data)
    data = fp.read(2)
# 关闭文件
fp.close()
new_fp.close()