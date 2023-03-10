# -*- coding: utf-8 -*-

import base64
import random
import string

def DexToHex(num):
    """十进制转为十六进制"""
    num = str(num)
    result = str(hex(eval(num)))
    return result
#混淆
def create_string_number(n):
    """生成一串指定位数的字符+数组混合的字符串"""
    m = random.randint(1, n)
    a = "".join([str(random.randint(0, 9)) for _ in range(m)])
    b = "".join([random.choice(string.ascii_letters) for _ in range(n - m)])
    return ''.join(random.sample(list(a + b), n))


#字典
def Dictionary(type1,i):
    """字典，实现数字字母转化,若type1是&则输出数字，type1是$则输出str"""
    if type1 == "&":
        out = ord(i)
    elif type1 == "$":
        out = chr(i)
    return out

def PwUncode(str1):
    """进行转化和补全，填充字符为 * ，每个字符以 | 分割"""
    i= 0
    a = ""
    while len(str1) > i:
        x = str1[i]
        x = ord(x)

        if x >10000:      
            x = DexToHex(x)
        if type(x)== type(123): 
            if x<1000 : 
                if x>=100:
                    revise = 6 - 3
                elif x>=10:
                    revise = 6 - 2
                elif x<10:
                    revise = 6 - 1 
                di = "******"
                j=0
                for asdsa in di:#补全
                    if revise == j:
                        break
                    x = asdsa+str(x)
                    j += 1
        print(x)
        a = a +"|"+ str(x)
        i += 1
    print("字符转化："+a)
    return a


def Pwhex(str1):
    """使用16进制加密"""

    allpw = ""#初始化
    for i in str1:
        a = i.encode().hex()
        print(a)
        if len(a) <=2:
            a = "&#" + str(a)
        allpw = str(allpw) + "|" +str(a)
    print("您加密的数据是："+allpw)
    return allpw

def Header(Pw1 = False):
    if Pw1 != False:
        x = random.randint(1,21)
        y = 21 - x
        z = 21 - y - x

        x = 80 +x
        y = 80 + y
        z = 80 + z
        head1 = str(chr(x)) + str(chr(y)) + str(chr(z))
    elif Pw1 == False:
        x = random.randint(21,42)    
        y = 42 - x
        z = 42 - y - x
        head1 = str(chr(x)) + str(chr(y)) + str(chr(z))
    head2 = create_string_number(3)
    head_all = str(head1) + str(head2)
    return head_all

def Pwm():
    """加密主区块"""
    Pws = input("请输入你要加密的文字")
    Pws = "&" + Pws;
    Pw = input("请输入你的密码（不输入则不设置密码），密码最低四位：")
    while 1: 
        if Pw == '' or False: Pw = False;break
        elif type(Pw) == type("asd"):
            if len(Pw) >=4:break
            else:
                Pw = input("密码不符合规格，请再次输入：")
    #加工head：
    if Pw != False:head_all_ = Header(Pw)
    if Pw == False:head_all_ = Header()
    #加工main：

    #main - head
    i = 0

    if Pw != False:
        main_head = 0
        while (len(Pw) > i):
            main_head1 = ord(Pw[i])
            i += 1 #每次增加 1 
            main_head = main_head + main_head1
        while main_head >= 10 :
            main_head = main_head -6   #解密时非常重要，请注意运算！
    else:
        main_head = create_string_number(6)
    print("main前缀混淆数："+str(main_head))

    #main - main
    main_showText = ""
    main_pwText = ""
    i = 0
    finally_return = ''
    while (len(Pws) >= i):
        try:
            main_showText = PwUncode(Pws[i+1])#因为Pws前为&：为什么？忘记了
            for num in main_showText:
                finally_return = finally_return + num
                finally_return = finally_return + create_string_number(ord(str(Pw[i])))

        except:break
        i += 1 

    
    print(head_all_+create_string_number(main_head)+finally_return+"\n完事")
    print(head_all_)
    # hexout1 = Pwhex(Pws);





def Unpwm():
    """解密主区块"""
    Pws = input("输入需要解密的文字")
    Psswitch = Pws[0:3]
    # i = 0     #四个四个切片的代码
    # while len(str1) >i :
    #     j= i +4
    #     print(str1[i:j])
    #     i = i+4


    a = base64.b16decode(finO.upper())





#---EFI---
SWI = input("解码（u）加密（l）")

#测试使用：



if SWI =="u":
    Unpwm()
elif SWI =="l":
    Pwm()


