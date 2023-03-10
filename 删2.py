a = 0
def DexToHex(num):
    """十进制转为十六进制"""
    num = str(num)
    # result = str(hex(eval(num)))
    result = ord(str(eval(num)))
    return result
print(DexToHex(a))
# str1 = "你好啊啊啊啊啊"

# def a(a):
#     print(a)

# i = 0
# while len(str1) > i:
#     try:a(str1[i+1]);
#     except:break
#     i += 1
# print(456)