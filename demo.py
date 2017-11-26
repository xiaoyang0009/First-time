# -*- coding：utf-8 -*-
'''
时间：20171125
作者：小杨
作用：第一次学习
''' 
'''
print("hello world!")

hstr="我是字符串"  #字符串
hnum=111  #数字
hlist=[1,2,3,"四","五"]  #数组
hdict={"a":"啊","b":"波"}  #字典
hfloat=3.1414  #浮点型
hnull=None #空

print(type(hstr))
'''
for i in range(4):
    if i != 3:
        print("-------------------------------------------")
        print("|                                          |")
        print("|--------欢迎登陆XX系统--------------------|")
        print("|                                          |")
        print("-------------------------------------------")

                    
        username = input("请输入账号: ")
        if username == "Tom":
            password = input("请输入密码: ")
            if password == "123456":
                print("登陆成功!")
                print("欢迎你，%s" % username)
                break
            else:
                print("密码错误!, 请重新登陆")
        else:
            print("对不起，账号不存在!")
    else:
         print("错误次数太多，登陆失败！")
         exit()
user = {"name": username, "age": "23岁", "high": "170cm", "job": "测试工程师","sex": "男"}
for Key in user:
    print(key, ":\t",user[Key])