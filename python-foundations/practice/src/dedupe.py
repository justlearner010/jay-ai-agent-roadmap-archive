#去重

nums =[1,2,2,3,3,4]

result = list(dict.fromkeys(nums))

print(result)
# 手动输入 【1，2，2，3，3，4】
#期望输出 [1,2,3,4]
#函数改写
def remove_duplicates(nums):
    if not nums:
        raise ValueError()
    return list(dict.fromkeys(nums))