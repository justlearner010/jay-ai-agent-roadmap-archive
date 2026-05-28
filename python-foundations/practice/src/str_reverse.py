
def str_reverse(str):
    lst = list(str)
    lst.reverse()
    
    rstr = "".join(lst)
    print(rstr)#.join可以把可迭代对象拼接为字符串
    return rstr #返回值为字符串类型


