def list_max(number):
    
    if not number:
        raise ValueError("没有值")
    lmax = max(number)
    return lmax #返回值为数字