"""
    将用户输入的文件复制一份,文件名为xxx-副本.xx
"""
# 让用户输入要复制的文件
filename = input("请输入你要复制的文件名:")
# 处理st得到复制后的文件名,从右边根据字符找到.的索引
num = filename.rindex(".")
# 用切片处理,拼接得到复制后的文件名
new_filename = filename[:num:]+"-副本"+filename[num::]
# 打开文件
fp = open(filename,"r",encoding="utf8")
new_fp = open(new_filename,"w",encoding="utf8")
# 操作文件
# 读取原文件里面的所有信息
data = fp.read()
# 将读取到的信息写入目标文件
new_fp.write(data)
# 关闭文件
fp.close()
new_fp.close()