# # -*- coding: utf-8 -*-

# # a = "123456789000"
# # i= 0

# # while len(a) >i :
# #     j= i +4
# #     print(a[i:j])
# #     i = i+4

# # import random


# # print(ord("\\"))
# # print(chr(0))

# # x = random.randint(1,21)
# # y = 21 - x
# # z = 21 - y - x

# # x = 80 +x
# # y = 80 + y
# # z = 80 + z

# # print(chr(x))
# # print(chr(y))
# # print(chr(z))
# str1 = input()

# def DexToHex(num):
#     """十进制转为十六进制"""
#     num = str(num)
#     result = str(hex(eval(num)))
#     return result

# def PwUncode(str1):
#     i= 0
#     a = ""
#     while len(str1) > i:
#         x = str1[i]
#         x = ord(x)

#         if x >10000:      
#             x = DexToHex(x)
#         if type(x)== type(123): 
#             if x<1000 : 
#                 if x>100:
#                     revise = 6 - 3
#                 elif x>10:
#                     revise = 6 - 2
#                 elif x<10:
#                     revise = 6 - 1 
#                 di = "******"
#                 j=0
#                 for asdsa in di:#补全
#                     if revise == j:
#                         break
#                     x = asdsa+str(x)
#                     j += 1
#         print(x)
#         a = a +"|"+ str(x)
#         i += 1
#     print("第一次加密内容为"+a)

# PwUncode(str1)
a = "123456789"
b = "abcdefghijklmnopqrstuvwx"
c = ''
d = 0 
e = 0
for i in a:

    if len(b)/4 >e :c = c+a[e]+b[d:d+4]
    else:pass
    d +=4
    e +=1

print(c)

