x = input("请输入一个整数")
def int_to_float(x):
    try:
        print(float(x))
    except ValueError:
        print("值不合法")
    except TypeError:
        print("无法转换类型")


int_to_float(x)