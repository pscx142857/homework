"""
2. 读取一个py文件，显示除了以井号(#)开头的行以外的所有行
"""
f = open("aa.py")
while True:
    a = f.readline()  # 读取下一行内容  a = "将 login.txt 的文件 复制一份\n"
    b = "#"
    if a == "":
        f.close()
        break
    elif a[0] == b[0]:
        continue
    else:
        print(a, end="")



# if __name__ == '__main__':
#     fp = open("aa.py", "r", encoding="utf8")
#     a = fp.readline()
#     print(a)
#     a = fp.readline()
#     print(a)
#     a = fp.readline()
#     print(a)
#     a = fp.readline()
#     print(a)