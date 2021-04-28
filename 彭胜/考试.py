"""
名片管理 系统

需要完成的功能 就是对 名片盒子 进行增删改查
    1. 添加名片: 根据用户录入的信息, 将信息添加到名片盒子里面
    2. 显示所有名片: 遍历名片盒子输出名片信息
    3. 修改名片:  录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,
        如果找到 , 重写录入新的名片信息, 完成修改操作
    4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.
"""
# 定义一个名片盒子,用的是列表,列表里面的元素是字典,这个字典就是一张一张的名片,存的是用户的信息
cards = [
    {"name": "莉莉", "tel": "13125018132", "company": "源码时代", "job": "秘书", "address": "天府新谷"},
    {"name": "丫丫", "tel": "13725488117", "company": "盛唐广告", "job": "经理", "address": "高新西区"},
    {"name": "霏霏", "tel": "18169471248", "company": "蚂蚁金服", "job": "测试", "address": "软件园D区"}
]

# 添加
def add():
    """
    根据用户输入的信息添加名片
    :return:
    """
    # 让用户输入添加的信息
    name = input("请输入姓名:")
    tel = input("请输入电话:")
    company = input("请输入公司名称:")
    job = input("请输入公司职位:")
    address = input("请输入公司地址:")
    # 用一张名片将用户输入的信息存起来,这个名片是个字典
    card = {"name":name,"tel":"tel","company":company,"job":job,"address":address}
    # 将这张名片添加到名片盒子(cards)里面
    cards.append(card)
    # 提示添加成功
    print("恭喜你添加成功")
# 显示
def show():
    """
    将名片盒子里面的名片展示出来
    :return:
    """
    # 打印表头
    print("姓名\t\t电话\t\t\t\t公司\t\t\t职位\t\t地址")
    # 循环遍历名片盒子,获取到一张一张的名片
    for card in cards:
        # 遍历名片,获取字典里面的值,然后显示出来
        for v in card.values():
            print(f"{v}\t\t",end="")
        print()
# 修改
def reverse():
    """
    根据用户输入的姓名修改名片
    :return:
    """
    # 让用户输入想修改的姓名
    name = input("请输入你要修改名片的姓名:")
    # 根据用户输入的姓名去找是否有这张名片,遍历名片盒子
    for card in cards:
        # 如果找到这张名片,就让用户输入新的信息,进行修改
        if card["name"] == name:
            name = input("请输入新的姓名:")
            tel = input("请输入新的电话:")
            company = input("请输入新的公司名称:")
            job = input("请输入新的公司职位:")
            address = input("请输入新的公司地址:")
            # 根据字典的键来修改
            card["name"] = name
            card["tel"] = tel
            card["company"] = company
            card["job"] = job
            card["address"] = address
            print("恭喜你修改成功")
            # 修改后直接结束遍历,跳出循环
            break
    else:
        # 没有找到,提示用户
        print("对不起,没有此人")
# 删除
def delete():
    """
    根据用户输入的姓名删除名片
    :return:
    """
    # 让用户输入想删除名片的姓名
    name = input("请输入你要删除名片的姓名:")
    # 根据用户输入的姓名去找是否有这张名片,遍历名片盒子
    for card in cards:
        # 如果找到这张名片,直接删除
        if card["name"] == name:
            cards.remove(card)
            print("恭喜你删除成功")
            # 删除后直接结束遍历,跳出循环
            break
    else:
        # 没有找到,提示用户
        print("对不起,没有此人")

# 主程序,死循环,让程序一直运行
while True:
    # 根据用户的输入选择功能
    st = input("请输入数字选择功能(1-添加 2-显示 3-修改 4-删除 5-退出):")

    # 根据用户输入的信息判断执行哪个功能
    if st == "1":
        # 调用添加函数
        add()
    elif st == "2":
        # 调用显示函数
        show()
    elif st == "3":
        # 调用修改函数
        reverse()
    elif st == "4":
        # 调用删除函数
        delete()
    elif st == "5":
        # 退出
        exit("退出系统")
    else:
        print("对不起,输入错误,请重新输入")